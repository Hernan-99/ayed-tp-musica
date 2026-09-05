# id, titulo, artista, album, genero, anio, duracion_seg

genre = [
    {"id": 1, "name": "Rock"},
    {"id": 2, "name": "Pop"},
    {"id": 3, "name": "Folklore"},
    {"id": 4, "name": "Cumbia"},
    {"id": 5, "name": "Urbano"},
    {"id": 6, "name": "Electronica"},
]

library = [
    {"id": 1, "titulo": "De Musica Ligera", "artista": "Soda Stereo", "album": "Cancion Animal", "genero": 1, "anio": 1990, "duracion_seg": 213},
    {"id": 2, "titulo": "Persiana Americana", "artista": "Soda Stereo", "album": "Signos", "genero": 1, "anio": 1986, "duracion_seg": 263},
    {"id": 3, "titulo": "En la Ciudad de la Furia", "artista": "Soda Stereo", "album": "Doble Vida", "genero": 1, "anio": 1988, "duracion_seg": 351},
    {"id": 4, "titulo": "Crimen", "artista": "Gustavo Cerati", "album": "Ahí vamos", "genero": 1, "anio": 2006, "duracion_seg": 239},
    {"id": 5, "titulo": "Adios", "artista": "Gustavo Cerati", "album": "Fuerza Natural", "genero": 1, "anio": 2009, "duracion_seg": 233},
    {"id": 6, "titulo": "Muchacha ojos de papel", "artista": "Luis Alberto Spinetta", "album": "Almendra", "genero": 1, "anio": 1969, "duracion_seg": 203},
    {"id": 7, "titulo": "Cantata de Puentes Amarillos", "artista": "Luis Alberto Spinetta", "album": "Artaud", "genero": 1, "anio": 1973, "duracion_seg": 557},
    {"id": 8, "titulo": "Rasguña las Piedras", "artista": "Sui Generis", "album": "Confesiones de Invierno", "genero": 1, "anio": 1973, "duracion_seg": 196},
    {"id": 9, "titulo": "Seminare", "artista": "Seru Giran", "album": "La Grasa de las Capitales", "genero": 1, "anio": 1979, "duracion_seg": 241},
    {"id": 10, "titulo": "Los Dinosaurios", "artista": "Charly Garcia", "album": "Clics Modernos", "genero": 1, "anio": 1983, "duracion_seg": 241},
    {"id": 11, "titulo": "Demoliendo Hoteles", "artista": "Charly Garcia", "album": "Piano Bar", "genero": 1, "anio": 1984, "duracion_seg": 151},
    {"id": 12, "titulo": "Jijiji", "artista": "Patricio Rey y sus Redonditos de Ricota", "album": "Un Baion para el Ojo Idiota", "genero": 1, "anio": 1988, "duracion_seg": 316},
    {"id": 13, "titulo": "Ji Ji Ji", "artista": "Patricio Rey y sus Redonditos de Ricota", "album": "En Directo", "genero": 1, "anio": 1992, "duracion_seg": 318},
    {"id": 14, "titulo": "La Bestia Pop", "artista": "Patricio Rey y sus Redonditos de Ricota", "album": "Oktubre", "genero": 1, "anio": 1986, "duracion_seg": 240},
    {"id": 15, "titulo": "Alfonsina y el mar", "artista": "Mercedes Sosa", "album": "Mujeres Argentinas", "genero": 3, "anio": 1969, "duracion_seg": 298},
    {"id": 16, "titulo": "Gracias a la Vida", "artista": "Mercedes Sosa", "album": "Hasta la Victoria", "genero": 3, "anio": 1971, "duracion_seg": 271},
    {"id": 17, "titulo": "La Balsa", "artista": "Los Gatos", "album": "Los Gatos", "genero": 1, "anio": 1967, "duracion_seg": 187},
    {"id": 18, "titulo": "El Extraño de Pelo Largo", "artista": "Almendra", "album": "Almendra", "genero": 1, "anio": 1969, "duracion_seg": 198},
    {"id": 19, "titulo": "Flaca", "artista": "Andres Calamaro", "album": "Honestidad Brutal", "genero": 1, "anio": 1999, "duracion_seg": 263},
    {"id": 20, "titulo": "Lamento Boliviano", "artista": "Los Enanitos Verdes", "album": "Big Bang", "genero": 1, "anio": 1994, "duracion_seg": 223},
    {"id": 21, "titulo": "La Guitarra", "artista": "Los Autenticos Decadentes", "album": "Mi Enfermedad", "genero": 4, "anio": 1997, "duracion_seg": 201},
    {"id": 22, "titulo": "Waka Waka", "artista": "Shakira", "album": "Sale el Sol", "genero": 2, "anio": 2010, "duracion_seg": 202},
    {"id": 23, "titulo": "Bzrp Music Sessions Vol. 52", "artista": "Bizarrap", "album": "Sessions", "genero": 5, "anio": 2022, "duracion_seg": 201},
    {"id": 24, "titulo": "Bzrp Music Sessions Vol. 53", "artista": "Bizarrap", "album": "Sessions", "genero": 5, "anio": 2023, "duracion_seg": 194},
    {"id": 25, "titulo": "Natacha", "artista": "Wos", "album": "Oscuro Extasis", "genero": 5, "anio": 2019, "duracion_seg": 183},
    {"id": 26, "titulo": "Canguros", "artista": "Wos", "album": "Tres Puntos Suspensivos", "genero": 5, "anio": 2021, "duracion_seg": 176},
    {"id": 27, "titulo": "Buenos Aires", "artista": "Nathy Peluso", "album": "Calambre", "genero": 5, "anio": 2020, "duracion_seg": 198},
    {"id": 28, "titulo": "Despecha", "artista": "Rosalia", "album": "Motomami", "genero": 2, "anio": 2022, "duracion_seg": 157},
    {"id": 29, "titulo": "Titi Me Pregunto", "artista": "Bad Bunny", "album": "Un Verano Sin Ti", "genero": 5, "anio": 2022, "duracion_seg": 243},
    {"id": 30, "titulo": "Anti-Hero", "artista": "Taylor Swift", "album": "Midnights", "genero": 2, "anio": 2022, "duracion_seg": 201},
    {"id": 31, "titulo": "Blank Space", "artista": "Taylor Swift", "album": "1989", "genero": 2, "anio": 2014, "duracion_seg": 231},
    {"id": 32, "titulo": "Bohemian Rhapsody", "artista": "Queen", "album": "A Night at the Opera", "genero": 1, "anio": 1975, "duracion_seg": 354},
    {"id": 33, "titulo": "Bohemian Rhapsody (Live Aid)", "artista": "Queen", "album": "Live Aid", "genero": 1, "anio": 1985, "duracion_seg": 362},
    {"id": 34, "titulo": "Don't Stop Me Now", "artista": "Queen", "album": "Jazz", "genero": 1, "anio": 1978, "duracion_seg": 209},
    {"id": 35, "titulo": "Come Together", "artista": "The Beatles", "album": "Abbey Road", "genero": 1, "anio": 1969, "duracion_seg": 259},
    {"id": 36, "titulo": "Here Comes the Sun", "artista": "The Beatles", "album": "Abbey Road", "genero": 1, "anio": 1969, "duracion_seg": 185},
    {"id": 37, "titulo": "Get Lucky", "artista": "Daft Punk", "album": "Random Access Memories", "genero": 6, "anio": 2013, "duracion_seg": 248},
    {"id": 38, "titulo": "One More Time", "artista": "Daft Punk", "album": "Discovery", "genero": 6, "anio": 2000, "duracion_seg": 320},
    {"id": 39, "titulo": "Rolling in the Deep", "artista": "Adele", "album": "21", "genero": 2, "anio": 2010, "duracion_seg": 228},
    {"id": 40, "titulo": "Someone Like You", "artista": "Adele", "album": "21", "genero": 2, "anio": 2011, "duracion_seg": 285},
    {"id": 41, "titulo": "Do I Wanna Know", "artista": "Arctic Monkeys", "album": "AM", "genero": 1, "anio": 2013, "duracion_seg": 272},
    {"id": 42, "titulo": "505", "artista": "Arctic Monkeys", "album": "Favourite Worst Nightmare", "genero": 1, "anio": 2007, "duracion_seg": 214},
    {"id": 43, "titulo": "Blinding Lights", "artista": "The Weeknd", "album": "After Hours", "genero": 2, "anio": 2019, "duracion_seg": 200},
    {"id": 44, "titulo": "Levitating", "artista": "Dua Lipa", "album": "Future Nostalgia", "genero": 2, "anio": 2020, "duracion_seg": 203},
    {"id": 45, "titulo": "As It Was", "artista": "Harry Styles", "album": "Harry's House", "genero": 2, "anio": 2022, "duracion_seg": 167},
    {"id": 46, "titulo": "Smells Like Teen Spirit", "artista": "Nirvana", "album": "Nevermind", "genero": 1, "anio": 1991, "duracion_seg": 301},
    {"id": 47, "titulo": "Wonderwall", "artista": "Oasis", "album": "What's the Story Morning Glory", "genero": 1, "anio": 1995, "duracion_seg": 258},
    {"id": 48, "titulo": "Wonderwall (Live)", "artista": "Oasis", "album": "Familiar to Millions", "genero": 1, "anio": 2000, "duracion_seg": 265},
    {"id": 49, "titulo": "Take On Me", "artista": "a-ha", "album": "Hunting High and Low", "genero": 2, "anio": 1985, "duracion_seg": 225},
    {"id": 50, "titulo": "Africa", "artista": "Toto", "album": "Toto IV", "genero": 2, "anio": 1982, "duracion_seg": 296},
    {"id": 51, "titulo": "Billie Jean", "artista": "Michael Jackson", "album": "Thriller", "genero": 2, "anio": 1982, "duracion_seg": 294},
    {"id": 52, "titulo": "Billie Jean (Remix)", "artista": "Michael Jackson", "album": "Thriller 40", "genero": 2, "anio": 2022, "duracion_seg": 292},
    {"id": 53, "titulo": "Clocks", "artista": "Coldplay", "album": "A Rush of Blood to the Head", "genero": 1, "anio": 2002, "duracion_seg": 307},
    {"id": 54, "titulo": "Yellow", "artista": "Coldplay", "album": "Parachutes", "genero": 1, "anio": 2000, "duracion_seg": 269},
    {"id": 55, "titulo": "Creep", "artista": "Radiohead", "album": "Pablo Honey", "genero": 1, "anio": 1992, "duracion_seg": 238},
    {"id": 56, "titulo": "Karma Police", "artista": "Radiohead", "album": "OK Computer", "genero": 1, "anio": 1997, "duracion_seg": 261},
    {"id": 57, "titulo": "Vino Griego", "artista": "Los Abuelos de la Nada", "album": "Vasos y Besos", "genero": 1, "anio": 1983, "duracion_seg": 214},
    {"id": 58, "titulo": "Lunes Por La Madrugada", "artista": "Los Abuelos de la Nada", "album": "Los Abuelos de la Nada", "genero": 1, "anio": 1982, "duracion_seg": 241},
    {"id": 59, "titulo": "El Aguante", "artista": "Divididos", "album": "Gol de Mujer", "genero": 1, "anio": 1998, "duracion_seg": 245},
    {"id": 60, "titulo": "Que Ves", "artista": "Divididos", "album": "Acariciando lo Aspero", "genero": 1, "anio": 1991, "duracion_seg": 232},
    {"id": 61, "titulo": "Gracias a la Vida", "artista": "Violeta Parra", "album": "Las Ultimas Composiciones", "genero": 3, "anio": 1966, "duracion_seg": 258},
    {"id": 62, "titulo": "De Musica Ligera (Unplugged)", "artista": "Soda Stereo", "album": "Comfort y Musica Para Volar", "genero": 1, "anio": 1996, "duracion_seg": 221},
    {"id": 63, "titulo": "Flaca (En vivo)", "artista": "Andres Calamaro", "album": "Vivo", "genero": 1, "anio": 2000, "duracion_seg": 270},
    {"id": 64, "titulo": "Creep (Live)", "artista": "Radiohead", "album": "The Astoria London", "genero": 1, "anio": 1994, "duracion_seg": 245},
    {"id": 65, "titulo": "Yellow (Live)", "artista": "Coldplay", "album": "Live 2003", "genero": 1, "anio": 2003, "duracion_seg": 280},
    {"id": 66, "titulo": "Blank Space (Acoustic)", "artista": "Taylor Swift", "album": "1989", "genero": 2, "anio": 2014, "duracion_seg": 228},
    {"id": 67, "titulo": "Get Lucky (Daft Punk Remix)", "artista": "Daft Punk", "album": "Random Access Memories", "genero": 6, "anio": 2013, "duracion_seg": 248},
]

def lists_songs():
    for song in library:
        print(
            f"Titulo: {song['titulo']}, "
            f"Artista: {song['artista']}, "
            f"Album: {song['album']}, "
            f"Genero: {song['genero']}, "
            f"Anio: {song['anio']}, "
            f"Duracion: {song['duracion_seg']} segundos"
        )


