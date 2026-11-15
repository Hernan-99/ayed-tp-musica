from pathlib import Path

from src.config import TEMA
from src.dominio.song import (
    Song,
    create_catalog_from_txt,
    load_version_relations,
    link_song_versions,
    lists_songs,
    show_version,
    song_to_dict,
)
from src.dominio.playlist import Playlist

from src.tads.pila import Pila
from src.tads.cola import Cola

from src.persistencia.binario import (
    guardar_binario,
    cargar_binario,
    alta_binario,
    baja_binario,
    actualizar_registro,
)
from src.persistencia.texto import guardar_texto

from src.excepciones import (
    ArchivoInvalidoError,
    ColeccionLlenaError,
    PilaVaciaError,
    ColaVaciaError,
)

from src.algoritmos.busqueda import (
    busqueda_lineal,
    busqueda_binaria,
)
from src.algoritmos.ordenamiento import (
    ordenar_insercion,
    ordenar_seleccion,
)


TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
}


def pendiente():
    print("Todavía no está implementado. Completar en la entrega que corresponde.")


def mostrar_menu():
    nombre = TEMAS.get(TEMA, TEMA or "(sin tema)")
    print()
    print(f"=== {nombre} — AyED C2 2026 ===")
    print("1. Listar catálogo")
    print("2. Ver detalle")
    print("3. Buscar")
    print("4. Ordenar")
    print("5. Operación recursiva")
    print("6. Colección principal (equipo / menú / playlist)")
    print("7. Historial (pila)")
    print("8. Cola")
    print("9. Guardar / cargar archivos")
    print("0. Salir")

#util
def save_catalog_text(catalog, data_dir):
    headers = [
        "id", "titulo", "artista", "album",
        "genero", "anio", "duracion_seg"
    ]

    rows = [song_to_dict(song) for song in catalog]

    guardar_texto(
        data_dir / "canciones_guardadas.txt",
        rows,
        headers
    )

def restore_song_versions(catalog, data_dir):
    relations = load_version_relations(data_dir / "versiones.txt")
    existing_ids = {song.id for song in catalog}

    valid_relations = [
        relation
        for relation in relations
        if relation["cancion_id"] in existing_ids
        and relation["version_de_id"] in existing_ids
    ]

    link_song_versions(catalog, valid_relations)

def main():
    # Validacion tema
    if TEMA not in TEMAS:
        print("Seteá TEMA en src/config.py: 'pokedex', 'recetario' o 'musica'.")
        return

    # carga del catálogo
    data_dir = Path(__file__).resolve().parents[1] / "data"
    binary_path = data_dir / "canciones.bin"

    if binary_path.exists():
        catalog = cargar_binario(binary_path)
    else:
        catalog = create_catalog_from_txt(data_dir / "canciones.txt")

    restore_song_versions(catalog, data_dir)

    library = list(catalog)

    print(f"Catalogo cargado: {catalog.tamanio()} canciones")

    playlist = Playlist(capacity=6)
    history = Pila()
    queue = Cola()

    opcion = None
    while opcion != "0":
        mostrar_menu()
        opcion = input("> ").strip()
        if opcion == "0":
            print("Chau.")
        elif opcion == "1":
            lists_songs(catalog)
        elif opcion == "3":
            print("=== Buscar cancion ===")
            print("1. Búsqueda lineal")
            print("2. Búsqueda binaria")
            print("0. Volver")
            action = input("> ").strip()

            if action in {"1", "2"}:
                title = input("Ingresar el titulo de la cancion: ").strip()
                if action == "1":
                    song = busqueda_lineal(
                        library,
                        title,
                        lambda item: item.titulo
                    )
                else:
                    ordered_library = library.copy()

                    ordenar_insercion(
                        ordered_library,
                        lambda item: item.titulo
                    )

                    print("Catalogo ordenado por titulo para realizar la busqueda.")
                    song = busqueda_binaria(
                        ordered_library,
                        title,
                        lambda item: item.titulo
                    )

                # mostrar resultado para ambas busquedas
                if song is not None:
                    print(f"Cancion encontrada: {song.titulo} - {song.artista}")
                else:
                    print("Cancion no encontrada")
        elif opcion == "4":
            print("=== Ordenar catálogo ===")
            print("1. Ordenar por título (selección)")
            print("2. Ordenar por año (inserción)")
            print("0. Volver")

            action = input("> ").strip()

            if action == "1":
                ordered_library = library.copy()

                ordenar_seleccion(
                    ordered_library,
                    lambda item: item.titulo
                )

                print("\nCatálogo ordenado por título:")

                for song in ordered_library:
                    print(f"{song.titulo} - {song.artista}")

            elif action == "2":
                ordered_library = library.copy()

                ordenar_insercion(
                    ordered_library,
                    lambda item: item.anio
                )

                print("\nCatálogo ordenado por año:")

                for song in ordered_library:
                    print(f"{song.anio} - {song.titulo} - {song.artista}")

            elif action != "0":
                print("Opción inválida.")
        elif opcion == "5":
            try:
                song_id = int(input("Ingrese el ID de la canción: "))
                show_version(song_id, catalog)
            except ValueError:
                print("Ingresá un ID numérico válido.")
        elif opcion == "6":
            print("1. Agregar canción")
            print("2. Listar playlist")
            action = input("> ").strip()

            if action == "1":
                try:
                    song_id = int(input("ID de la canción para agregar a la playlist: "))
                    song = next(
                        (item for item in library if item.id == song_id),
                        None,
                    )

                    if song is None:
                        print("Canción no encontrada.")
                    else:
                        playlist.agregar(song)
                        print(f"Agregada: {song.titulo}")

                except ColeccionLlenaError as error:
                    print(f"Error: {error}")
                except ValueError:
                    print("Ingresá un ID numérico válido.")

            elif action == "2":
                if playlist.esta_vacia():
                    print("La playlist está vacía.")
                else:
                    for song in playlist:
                        print(f"{song.id}. {song.titulo} - {song.artista}")

            else:
                print("Opción inválida.")
        elif opcion == "7":
            print("1. Registrar canción en el historial")
            print("2. Ver última canción")
            print("3. Desapilar última canción")
            action = input("> ").strip()

            if action == "1":
                try:
                    song_id = int(input("ID de la canción: "))
                    song = next(
                        (item for item in library if item.id == song_id),
                        None,
                    )

                    if song is None:
                        print("Canción no encontrada.")
                    else:
                        history.apilar(song)
                        print(f"Agregada al historial: {song.titulo}")

                except ValueError:
                    print("Ingresá un ID numérico válido.")

            elif action == "2":
                try:
                    song = history.ver_tope()
                    print(f"Última canción: {song.titulo}")
                except PilaVaciaError as error:
                    print(error)

            elif action == "3":
                try:
                    song = history.desapilar()
                    print(f"Retirada del historial: {song.titulo}")
                except PilaVaciaError as error:
                    print(error)

            else:
                print("Opción inválida.")
        elif opcion == "8":
            print("1. Agregar canción a la cola")
            print("2. Reproducir siguiente canción")
            print("3. Ver próxima canción")
            print("4. Listar canciones pendientes")
            action = input("> ").strip()
            if action == "1":
                try:
                    song_id = int(input("ID de la canción: "))
                    song = next(
                        (item for item in library if item.id == song_id),
                        None,
                    )

                    if song is None:
                        print("Canción no encontrada.")
                    else:
                        queue.encolar(song)
                        print(f"Encolada: {song.titulo}")

                except ValueError:
                    print("Ingresá un ID numérico válido.")
            elif action == "2":
                try:
                    song = queue.desencolar()
                    history.apilar(song)
                    print(f"Reproduciendo: {song.titulo}")
                except ColaVaciaError as error:
                    print(error)
            elif action == "3":
                try:
                    print(f"Próxima canción: {queue.ver_frente().titulo}")
                except ColaVaciaError as error:
                    print(error)
            elif action == "4":
                if queue.esta_vacia():
                    print("La cola está vacía.")
                else:
                    for song in queue:
                        print(f"{song.id}. {song.titulo} - {song.artista}")
        elif opcion == "9":
            print("=== Persistencia binaria ===")
            print("1. Guardar catálogo")
            print("2. Cargar catálogo")
            print("3. Agregar canción")
            print("4. Eliminar canción")
            print("5. Modificar canción")
            print("0. Volver")
            action = input("> ").strip()

            try:
                if action == "1":
                    save_catalog_text(catalog, data_dir)
                    guardar_binario(binary_path, catalog)
                    print("Catálogo guardado en texto y binario correctamente.")
                elif action == "2":
                    catalog = cargar_binario(binary_path)

                    restore_song_versions(catalog, data_dir)

                    library = list(catalog)
                    print(
                        f"Catálogo cargado: {catalog.tamanio()} canciones."
                    )
                elif action == "3":
                    print("=== Agregar canción ===")

                    try:
                        song_id = int(input("ID: "))
                        title = input("Título: ").strip()
                        artist = input("Artista: ").strip()
                        album = input("Álbum: ").strip()
                        genre = int(input("Género (1-6): "))
                        year = int(input("Año: "))
                        duration = int(input("Duración en segundos: "))

                    except ValueError:
                        print("Error: ingresá números válidos en los campos numéricos.")

                    else:
                        if (
                            song_id <= 0
                            or not title
                            or not artist
                            or not album
                            or genre not in range(1, 7)
                            or year <= 0
                            or not 0 <= duration <= 65535
                        ):
                            print("Error: los datos ingresados no son válidos.")

                        elif any(song.id == song_id for song in catalog):
                            print(f"Error: ya existe una canción con ID {song_id}.")

                        else:
                            new_song = Song(
                                id=song_id,
                                titulo=title,
                                artista=artist,
                                album=album,
                                genero=genre,
                                anio=year,
                                duracion_seg=duration,
                            )

                            # Crear el binario si todavia no existe
                            if not binary_path.exists():
                                guardar_binario(binary_path, catalog)

                            # Persistir primero, actualizar memoria solo si funciona
                            alta_binario(binary_path, new_song)

                            catalog.insertar_al_final(new_song)
                            library = list(catalog)

                            save_catalog_text(catalog, data_dir)

                            print("Canción agregada y guardada correctamente.")
                elif action == "4":
                    print("=== Eliminar canción ===")
                    try:
                        song_id = int(input("ID de la canción a eliminar: "))
                    except ValueError:
                                print("Error: ingresá un ID numérico.")
                    else:
                        song = next(
                        (item for item in catalog if item.id == song_id),None)
                        if song is None:
                            print(f"No existe una canción con ID {song_id}.")
                        else:
                            print(f"Canción encontrada: {song.titulo} - {song.artista}")
                            confirm = input("¿Confirmar eliminación? (s/n): ").strip().lower()

                            if confirm == "s":
                                if not binary_path.exists():
                                    guardar_binario(binary_path, catalog)

                                # Persistir primero.
                                baja_binario(binary_path, song_id)

                                # Recuperar el catálogo actualizado.
                                catalog = cargar_binario(binary_path)

                                restore_song_versions(catalog, data_dir)
                                library = list(catalog)

                                save_catalog_text(catalog, data_dir)

                                print("Canción eliminada correctamente.")

                            else:
                                print("Eliminación cancelada.")
                elif action == "5":
                    print("=== Modificar canción ===")

                    try:
                        song_id = int(input("ID de la canción a modificar: "))
                    except ValueError:
                        print("Error: ingresá un ID numérico.")
                    else:
                        songs = list(catalog)

                        position = next(
                            (index for index, song in enumerate(songs)
                            if song.id == song_id),
                            None
                        )

                        if position is None:
                            print(f"No existe una canción con ID {song_id}.")

                        else:
                            current_song = songs[position]

                            print(f"Canción: {current_song.titulo} - {current_song.artista}")
                            print("Dejá el campo vacío para conservar su valor.")

                            title = input(f"Título [{current_song.titulo}]: ").strip()
                            artist = input(f"Artista [{current_song.artista}]: ").strip()
                            album = input(f"Álbum [{current_song.album}]: ").strip()

                            try:
                                genre_input = input(
                                    f"Género (1-6) [{current_song.genero}]: "
                                ).strip()
                                year_input = input(
                                    f"Año [{current_song.anio}]: "
                                ).strip()
                                duration_input = input(
                                    f"Duración [{current_song.duracion_seg}]: "
                                ).strip()

                                genre = (
                                    int(genre_input) if genre_input
                                    else current_song.genero
                                )
                                year = (
                                    int(year_input) if year_input
                                    else current_song.anio
                                )
                                duration = (
                                    int(duration_input) if duration_input
                                    else current_song.duracion_seg
                                )

                            except ValueError:
                                print("Error: ingresá valores numéricos válidos.")

                            else:
                                updated_song = Song(
                                    id=current_song.id,
                                    titulo=title or current_song.titulo,
                                    artista=artist or current_song.artista,
                                    album=album or current_song.album,
                                    genero=genre,
                                    anio=year,
                                    duracion_seg=duration,
                                )

                                if (
                                    updated_song.genero not in range(1, 7)
                                    or not 0 <= updated_song.anio <= 65535
                                    or not 0 <= updated_song.duracion_seg <= 65535
                                ):
                                    print("Error: los datos ingresados no son válidos.")

                                else:
                                    if not binary_path.exists():
                                        guardar_binario(binary_path, catalog)

                                    # Modificar únicamente el registro correspondiente.
                                    actualizar_registro(
                                        binary_path,
                                        position,
                                        updated_song
                                    )

                                    # Recargar y sincronizar el catálogo en memoria.
                                    catalog = cargar_binario(binary_path)

                                    restore_song_versions(catalog, data_dir)
                                    library = list(catalog)

                                    save_catalog_text(catalog, data_dir)

                                    print("Canción modificada correctamente.")
            except ArchivoInvalidoError as e:
                print(f"Error de persistencia: {e}")
        elif opcion in {"2"}:
            pendiente()
        else:
            print("Opcion invalida.")

if __name__ == "__main__":
    main()
