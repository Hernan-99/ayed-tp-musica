from src.persistencia.texto import cargar_texto
from src.tads.lista_enlazada import ListaEnlazada
from src.excepciones import ArchivoInvalidoError


class Song:
    # metodo constructor.
    def __init__(self,
                 id: int,
                 titulo: str,
                 artista: str,
                 album: str,
                 genero: int,
                 anio: int,
                 duracion_seg: int,
                 version_derivada:list | None = None # si no tien version derivada
                 ):

        # atributos
        self.id = id
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.genero = genero
        self.anio = anio
        self.duracion_seg = duracion_seg
        self.version_derivada = [] if version_derivada is None else version_derivada

def create_catalog_from_txt(ruta):
    """Construye un catálogo de canciones desde un archivo de texto."""
    catalog = ListaEnlazada()
    genres = {
        "Rock": 1,
        "Pop": 2,
        "Folklore": 3,
        "Cumbia": 4,
        "Urbano": 5,
        "Electronica": 6,
    }

    for row in cargar_texto(ruta):
        try:
            genre_id = genres[row["genero"]]
            song = Song(
                id=int(row["id"]),
                titulo=row["titulo"],
                artista=row["artista"],
                album=row["album"],
                genero=genre_id,
                anio=int(row["anio"]),
                duracion_seg=int(row["duracion_seg"]),
            )
        except (KeyError, ValueError) as e:
            raise ArchivoInvalidoError(
                f"Error: {e}. Registro de canción inválido: {row}"
            )
        catalog.insertar_al_final(song)

    return catalog


def lists_songs(catalog):
    for song in catalog:
        print(
            f"Titulo: {song.titulo}, "
            f"Artista: {song.artista}, "
            f"Album: {song.album}, "
            f"Genero: {song.genero}, "
            f"Anio: {song.anio}, "
            f"Duracion: {song.duracion_seg} segundos"
        )

        if song.version_derivada: # si esto valida en true
            print("Versiones derivadas:")
            for v_id in song.version_derivada:
                version = get_by_id(v_id, catalog)

                if version is not None: # si se encuentra cancion, asocio a id
                    print(version.titulo, version.artista, version.album, version.genero, version.anio, str(version.duracion_seg) + " segundos")

def get_by_id(song_id: int, catalog):
    for song in catalog:
        if song.id == song_id:
            return song
    return None

def show_version(song_id: int, catalog):

    song = get_by_id(song_id, catalog)

    if song is None: # Si la cancion no existe, muestro mensaje de error
        print("Cancion no encontrada")
        return

    print(
        f"Titulo: {song.titulo}, "
        f"Artista: {song.artista}, "
        f"Album: {song.album}, "
        f"Genero: {song.genero}, "
        f"Anio: {song.anio}, "
        f"Duracion: {song.duracion_seg} segundos"
    )

    for version_id in song.version_derivada:
        show_version(version_id, catalog)

def load_version_relations(ruta):
    #lee  relaciones entre canciones y sus versiones
    relations = []

    for row in cargar_texto(ruta):
        try:
            relations.append({
                "cancion_id": int(row["cancion_id"]),
                "version_de_id": int(row["version_de_id"]),
                "tipo": row["tipo"]
            })
        except (KeyError, ValueError):
            raise ArchivoInvalidoError(
                f"Relacion de version invalida: {row}"
            )

    return relations

def link_song_versions(catalog, relations):
    # Asocia cada version derivada con cancion la original
    song_by_id = {song.id: song for song in catalog}

    for relation in relations:
        version_id = relation["cancion_id"]
        original_id = relation["version_de_id"]

        if original_id not in song_by_id or version_id not in song_by_id:
            raise ArchivoInvalidoError(
                f"Relacion invalida: {original_id} : {version_id}"
            )
        original_song = song_by_id[original_id]
        if version_id not in original_song.version_derivada:
            original_song.version_derivada.append(version_id)

def song_to_dict(song):
    #Convierte un obj Song a un registro compatible con canciones.txt
    genres = {
        1: "Rock",
        2: "Pop",
        3: "Folklore",
        4: "Cumbia",
        5: "Urbano",
        6: "Electronica",
    }

    if song.genero not in genres:
        raise ArchivoInvalidoError(f"Genero invalido para {song.id}: {song.genero}")

    return {
        "id": song.id,
        "titulo": song.titulo,
        "artista": song.artista,
        "album": song.album,
        "genero": genres[song.genero],
        "anio": song.anio,
        "duracion_seg": song.duracion_seg
    }
