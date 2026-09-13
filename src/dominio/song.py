# id, titulo, artista, album, genero, anio, duracion_seg


# LEGACY
genre = [
    {"id": 1, "name": "Rock"},
    {"id": 2, "name": "Pop"},
    {"id": 3, "name": "Folklore"},
    {"id": 4, "name": "Cumbia"},
    {"id": 5, "name": "Urbano"},
    {"id": 6, "name": "Electronica"},
]

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



library = [
    Song(1, "De Musica Ligera", "Soda Stereo", "Cancion Animal", 1, 1990, 213, [62]),
    Song(2, "Persiana Americana", "Soda Stereo", "Signos", 1, 1986, 263),
    Song(3, "En la Ciudad de la Furia", "Soda Stereo", "Doble Vida", 1, 1988, 351),
    Song(4, "Crimen", "Gustavo Cerati", "Ahí vamos", 1, 2006, 239),
    Song(5, "Adios", "Gustavo Cerati", "Fuerza Natural", 1, 2009, 233),
    Song(6, "Muchacha ojos de papel", "Luis Alberto Spinetta", "Almendra", 1, 1969, 203),
    Song(7, "Cantata de Puentes Amarillos", "Luis Alberto Spinetta", "Artaud", 1, 1973, 557),
    Song(8, "Rasguña las Piedras", "Sui Generis", "Confesiones de Invierno", 1, 1973, 196),
    Song(9, "Seminare", "Seru Giran", "La Grasa de las Capitales", 1, 1979, 241),
    Song(10, "Los Dinosaurios", "Charly Garcia", "Clics Modernos", 1, 1983, 241),
    Song(11, "Demoliendo Hoteles", "Charly Garcia", "Piano Bar", 1, 1984, 151),
    Song(12, "Jijiji", "Patricio Rey y sus Redonditos de Ricota", "Un Baion para el Ojo Idiota", 1, 1988, 316, [13]),
    Song(13, "Ji Ji Ji", "Patricio Rey y sus Redonditos de Ricota", "En Directo", 1, 1992, 318),
    Song(14, "La Bestia Pop", "Patricio Rey y sus Redonditos de Ricota", "Oktubre", 1, 1986, 240),
    Song(15, "Alfonsina y el mar", "Mercedes Sosa", "Mujeres Argentinas", 3, 1969, 298),
    Song(16, "Gracias a la Vida", "Mercedes Sosa", "Hasta la Victoria", 3, 1971, 271, [61]),
    Song(17, "La Balsa", "Los Gatos", "Los Gatos", 1, 1967, 187),
    Song(18, "El Extraño de Pelo Largo", "Almendra", "Almendra", 1, 1969, 198),
    Song(19, "Flaca", "Andres Calamaro", "Honestidad Brutal", 1, 1999, 263, [63]),
    Song(20, "Lamento Boliviano", "Los Enanitos Verdes", "Big Bang", 1, 1994, 223),
    Song(21, "La Guitarra", "Los Autenticos Decadentes", "Mi Enfermedad", 4, 1997, 201),
    Song(22, "Waka Waka", "Shakira", "Sale el Sol", 2, 2010, 202),
    Song(23, "Bzrp Music Sessions Vol. 52", "Bizarrap", "Sessions", 5, 2022, 201),
    Song(24, "Bzrp Music Sessions Vol. 53", "Bizarrap", "Sessions", 5, 2023, 194),
    Song(25, "Natacha", "Wos", "Oscuro Extasis", 5, 2019, 183),
    Song(26, "Canguros", "Wos", "Tres Puntos Suspensivos", 5, 2021, 176),
    Song(27, "Buenos Aires", "Nathy Peluso", "Calambre", 5, 2020, 198),
    Song(28, "Despecha", "Rosalia", "Motomami", 2, 2022, 157),
    Song(29, "Titi Me Pregunto", "Bad Bunny", "Un Verano Sin Ti", 5, 2022, 243),
    Song(30, "Anti-Hero", "Taylor Swift", "Midnights", 2, 2022, 201),
    Song(31, "Blank Space", "Taylor Swift", "1989", 2, 2014, 231,[66]),
    Song(32, "Bohemian Rhapsody", "Queen", "A Night at the Opera", 1, 1975, 354, [33]),
    Song(33, "Bohemian Rhapsody (Live Aid)", "Queen", "Live Aid", 1, 1985, 362),
    Song(34, "Don't Stop Me Now", "Queen", "Jazz", 1, 1978, 209),
    Song(35, "Come Together", "The Beatles", "Abbey Road", 1, 1969, 259),
    Song(36, "Here Comes the Sun", "The Beatles", "Abbey Road", 1, 1969, 185),
    Song(37, "Get Lucky", "Daft Punk", "Random Access Memories", 6, 2013, 248, [67]),
    Song(38, "One More Time", "Daft Punk", "Discovery", 6, 2000, 320),
    Song(39, "Rolling in the Deep", "Adele", "21", 2, 2010, 228),
    Song(40, "Someone Like You", "Adele", "21", 2, 2011, 285),
    Song(41, "Do I Wanna Know", "Arctic Monkeys", "AM", 1, 2013, 272),
    Song(42, "505", "Arctic Monkeys", "Favourite Worst Nightmare", 1, 2007, 214),
    Song(43, "Blinding Lights", "The Weeknd", "After Hours", 2, 2019, 200),
    Song(44, "Levitating", "Dua Lipa", "Future Nostalgia", 2, 2020, 203),
    Song(45, "As It Was", "Harry Styles", "Harry's House", 2, 2022, 167),
    Song(46, "Smells Like Teen Spirit", "Nirvana", "Nevermind", 1, 1991, 301),
    Song(47, "Wonderwall", "Oasis", "What's the Story Morning Glory", 1, 1995, 258, [48]),
    Song(48, "Wonderwall (Live)", "Oasis", "Familiar to Millions", 1, 2000, 265),
    Song(49, "Take On Me", "a-ha", "Hunting High and Low", 2, 1985, 225),
    Song(50, "Africa", "Toto", "Toto IV", 2, 1982, 296),
    Song(51, "Billie Jean", "Michael Jackson", "Thriller", 2, 1982, 294, [52]),
    Song(52, "Billie Jean (Remix)", "Michael Jackson", "Thriller 40", 2, 2022, 292),
    Song(53, "Clocks", "Coldplay", "A Rush of Blood to the Head", 1, 2002, 307),
    Song(54, "Yellow", "Coldplay", "Parachutes", 1, 2000, 269, [65]),
    Song(55, "Creep", "Radiohead", "Pablo Honey", 1, 1992, 238, [64]),
    Song(56, "Karma Police", "Radiohead", "OK Computer", 1, 1997, 261),
    Song(57, "Vino Griego", "Los Abuelos de la Nada", "Vasos y Besos", 1, 1983, 214),
    Song(58, "Lunes Por La Madrugada", "Los Abuelos de la Nada", "Los Abuelos de la Nada", 1, 1982, 241),
    Song(59, "El Aguante", "Divididos", "Gol de Mujer", 1, 1998, 245),
    Song(60, "Que Ves", "Divididos", "Acariciando lo Aspero", 1, 1991, 232),
    Song(61, "Gracias a la Vida", "Violeta Parra", "Las Ultimas Composiciones", 3, 1966, 258),
    Song(62, "De Musica Ligera (Unplugged)", "Soda Stereo", "Comfort y Musica Para Volar", 1, 1996, 221),
    Song(63, "Flaca (En vivo)", "Andres Calamaro", "Vivo", 1, 2000, 270),
    Song(64, "Creep (Live)", "Radiohead", "The Astoria London", 1, 1994, 245),
    Song(65, "Yellow (Live)", "Coldplay", "Live 2003", 1, 2003, 280),
    Song(66, "Blank Space (Acoustic)", "Taylor Swift", "1989", 2, 2014, 228),
    Song(67, "Get Lucky (Daft Punk Remix)", "Daft Punk", "Random Access Memories", 6, 2013, 248),
]

def lists_songs():
    for song in library:
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
                version = get_by_id(v_id)

                if version is not None: # si se encuentra cancion, asocio a id
                    print(version.titulo, version.artista, version.album, version.genero, version.anio, str(version.duracion_seg) + " segundos")


def get_by_id(id:int):
    for song in library:
        if song.id == id:
            return song
    return None


def show_version(id:int):

    # Busco cancion segun el id que es pasad
    song = get_by_id(id)

    if song is not None: # Si la cancion existe, muestro los datos
        print(f"Titulo: {song.titulo}, Artista: {song.artista}, Album: {song.album}, Genero: {song.genero}, Anio: {song.anio}, Duracion: {song.duracion_seg} segundos")

        # bucle para recorrer id's de las versiones derivadas, dos casos:
        # 1. si la lista esta vacia termina el bucle y termina la funcion
        for version_id in song.version_derivada:
                # 2.  recursividad: vuelve a ejecutar la funcion para cada version derivada
                show_version(version_id)
    else:
        # Se ejecuta si el ID que se pasa no corresponde a ninguna cancion
        print("Cancion no encontrada")
