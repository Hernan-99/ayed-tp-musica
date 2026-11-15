import struct
from pathlib import Path

from src.excepciones import ArchivoInvalidoError
"""Registros de longitud fija con struct.

Layout sugerido (documentar el definitivo en docs/INFORME.md):

Header:
  magia     4s   b'AYED'
  tema      1s   b'P' | b'R' | b'M'
  cantidad  I    unsigned int

El registro depende del tema. Ejemplo Pokédex:
  id          I
  nombre     20s
  tipo1      12s
  tipo2      12s
  hp          H
  ataque      H
  defensa     H
  velocidad   H
  generacion  H
"""



MAGIC = b"AYED"
THEME = b"M"

HEADER = struct.Struct("<4s 1s I")
RECORD = struct.Struct("<I 30s 60s 30s 12s 2H")

GENRES = {
    1: "Rock",
    2: "Pop",
    3: "Folklore",
    4: "Cumbia",
    5: "Urbano",
    6: "Electronica",
}

def encode_text(value, size):
    """Codifica texto UTF-8 y completa el campo con bytes nulos."""
    encoded = value.encode("utf-8")

    if len(encoded) > size:
        raise ArchivoInvalidoError(
            f"El texto '{value}' supera el limite de {size} bytes."
        )

    return encoded.ljust(size, b"\x00")


def pack_song(song):
    """Convierte una canción en un registro binario fijo."""
    try:
        genre = GENRES[song.genero]

        return RECORD.pack(
            song.id,
            encode_text(song.titulo, 30),
            encode_text(song.artista, 60),
            encode_text(song.album, 30),
            encode_text(genre, 12),
            song.anio,
            song.duracion_seg,
        )
    except (KeyError, struct.error, OverflowError, TypeError) as e:
        raise ArchivoInvalidoError(
            f"No se pudo codificar la canción {song.id}. Error: {e}."
        )

# util
def decode_text(value):
    #Decodifica texto UTF-8 y elimina bytes nulos
    return value.rstrip(b"\x00").decode("utf-8")


def guardar_binario(ruta, items):
    #Guarda cabecera y registros de longitud fija.
    route = Path(ruta)

    records = [pack_song(song) for song in items]
    try:
        with route.open("wb") as file:
            file.write(HEADER.pack(MAGIC, THEME, len(records)))

            for record in records:
                file.write(record)

    except OSError as e:
        raise ArchivoInvalidoError(
            f"No se pudo guardar el archivo binario: {route}. Error: {e}"
        )

def cargar_binario(ruta):
    # Carga canciones desde un archivo binario de registros fijos
    from src.dominio.song import Song
    from src.tads.lista_enlazada import ListaEnlazada

    route = Path(ruta)
    catalog = ListaEnlazada()

    genre_ids = {name: code for code, name in GENRES.items()}

    try:
        with route.open("rb") as file:
            header_data = file.read(HEADER.size)

            if len(header_data) != HEADER.size:
                raise ArchivoInvalidoError(
                    "La cabecera del archivo binario esta incompleta"
                )

            magic, theme, count = HEADER.unpack(header_data)

            if magic != MAGIC or theme != THEME:
                raise ArchivoInvalidoError(
                    "La cabecera del archivo binario es invalida"
                )

            for position in range(count):
                record_data = file.read(RECORD.size)

                if len(record_data) != RECORD.size:
                    raise ArchivoInvalidoError(
                        f"Registro incompleto en la posicion {position}."
                    )

                (
                    song_id,
                    title,
                    artist,
                    album,
                    genre,
                    year,
                    duration,
                ) = RECORD.unpack(record_data)

                genre_name = decode_text(genre)

                if genre_name not in genre_ids:
                    raise ArchivoInvalidoError(
                        f"Genero invalido en la posicion {position}."
                    )

                song = Song(
                    id=song_id,
                    titulo=decode_text(title),
                    artista=decode_text(artist),
                    album=decode_text(album),
                    genero=genre_ids[genre_name],
                    anio=year,
                    duracion_seg=duration,
                )

                catalog.insertar_al_final(song)

            if file.read(1):
                raise ArchivoInvalidoError(
                    "El archivo contiene datos adicionales"
                )

    except (OSError, UnicodeError, struct.error) as e:
        raise ArchivoInvalidoError(
            f"No se pudo cargar el archivo binario: {route}. Error: {e}"
        )

    return catalog

def actualizar_registro(ruta, posicion, item):
    """Pisa un registro por posición (acceso directo). posicion es 0-based."""

    # Actualiza un registro por posición sin reescribir el archivo
    route = Path(ruta)

    if not isinstance(posicion, int) or isinstance(posicion, bool):
        raise ArchivoInvalidoError("La posicion debe ser un numero entero")

    if posicion < 0:
        raise ArchivoInvalidoError("La posicion no puede ser negativa")

    record_data = pack_song(item)

    try:
        with route.open("r+b") as file:
            header_data = file.read(HEADER.size)

            if len(header_data) != HEADER.size:
                raise ArchivoInvalidoError(
                    "La cabecera esta incompleta"
                )

            magic, theme, count = HEADER.unpack(header_data)

            if magic != MAGIC or theme != THEME:
                raise ArchivoInvalidoError(
                    "La cabecera es invalida"
                )

            if posicion >= count:
                raise ArchivoInvalidoError(
                    f"Posicion fuera de rango: {posicion}."
                )

            file.seek(0, 2)
            expected_size = HEADER.size + count * RECORD.size

            if file.tell() != expected_size:
                raise ArchivoInvalidoError(
                    "El tamaño del archivo no coincide con su cabecera"
                )

            offset = HEADER.size + posicion * RECORD.size
            file.seek(offset)
            file.write(record_data)

    except OSError as e:
        raise ArchivoInvalidoError(
            f"No se pudo actualizar el registro: {route}. Error: {e}"
        )

def alta_binario(ruta, item):
    #Agrega una cancian al final del archivo binario
    route = Path(ruta)
    record_data = pack_song(item)

    try:
        with route.open("r+b") as file:
            header_data = file.read(HEADER.size)

            if len(header_data) != HEADER.size:
                raise ArchivoInvalidoError(
                    "Cabecera incompleta"
                )

            magic, theme, count = HEADER.unpack(header_data)

            if magic != MAGIC or theme != THEME:
                raise ArchivoInvalidoError(
                    "Cabecera invalida"
                )

            file.seek(0, 2)

            expected_size = HEADER.size + count * RECORD.size

            if file.tell() != expected_size:
                raise ArchivoInvalidoError(
                    "Tamaño del archivo invalido"
                )

            # Evitar canciones con IDs duplicados
            file.seek(HEADER.size)

            for _ in range(count):
                existing_record = file.read(RECORD.size)
                existing_id = RECORD.unpack(existing_record)[0]

                if existing_id == item.id:
                    raise ArchivoInvalidoError(
                        f"Ya existe una canción con el ID {item.id}."
                    )

            # Agregar el registro al final
            file.seek(0, 2)
            file.write(record_data)

            # Actualizar la cantidad de canciones en la cabecera
            file.seek(0)
            file.write(HEADER.pack(MAGIC, THEME, count + 1))

    except OSError as e:
        raise ArchivoInvalidoError(
            f"No se pudo agregar la canción: {route}. Error: {e}"
        )


def baja_binario(ruta, song_id):
    #Elimina una cancion por ID y actualiza el archivo binario
    route = Path(ruta)

    catalog = cargar_binario(route)

    remaining = []
    found = False

    for song in catalog:
        if song.id == song_id:
            found = True
        else:
            remaining.append(song)

    if not found:
        raise ArchivoInvalidoError(
            f"No existe una cancion con ID {song_id}"
        )

    guardar_binario(route, remaining)
