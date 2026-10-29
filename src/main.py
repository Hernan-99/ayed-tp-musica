from src.config import TEMA
from src.dominio.song import lists_songs, show_version, library
from src.dominio.playlist import Playlist
from src.tads.pila import Pila
from src.tads.cola import Cola
from src.excepciones import (
    ColeccionLlenaError,
    PilaVaciaError,
    ColaVaciaError,
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


def main():
    if TEMA not in TEMAS:
        print("Seteá TEMA en src/config.py: 'pokedex', 'recetario' o 'musica'.")
        return

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
            lists_songs()
        elif opcion == "5":
            try:
                song_id = int(input("Ingrese el ID de la canción: "))
                show_version(song_id)
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
        elif opcion in {"2", "3", "4", "9"}:
            pendiente()
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
