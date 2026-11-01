
import time

from src.dominio.song import library
from src.algoritmos.busqueda import busqueda_lineal, busqueda_binaria
from src.algoritmos.ordenamiento import ordenar_seleccion, ordenar_insercion


def measure_search(function, collection, key, get_key, repetitions=1000):
    start = time.perf_counter()

    for _ in range(repetitions):
        function(collection, key, get_key)

    end = time.perf_counter()

    return (end - start) / repetitions


def measure_sort(function, collection, get_key, repetitions=5):
    total_time = 0

    for _ in range(repetitions):
        data = collection.copy()

        start = time.perf_counter()
        function(data, get_key)
        end = time.perf_counter()

        total_time += end - start

    return total_time / repetitions


def main():
    original_library = library.copy()
    enlarged_library = library * 10

    datasets = {
        "Original (67 canciones)": original_library,
        "Ampliado (670 canciones)": enlarged_library,
    }

    missing_title = "ZZZ - Cancion inexistente"

    print("\n=== MEDICIONES DE COMPLEJIDAD ===")

    for name, dataset in datasets.items():
        print(f"\n--- {name} ---")

        # Preparamos una copia ordenada para la búsqueda binaria.
        ordered_library = dataset.copy()

        ordenar_insercion(
            ordered_library,
            lambda song: song.titulo
        )

        # Búsqueda lineal.
        linear_time = measure_search(
            busqueda_lineal,
            dataset,
            missing_title,
            lambda song: song.titulo
        )

        # Búsqueda binaria.
        binary_time = measure_search(
            busqueda_binaria,
            ordered_library,
            missing_title,
            lambda song: song.titulo
        )

        # Ordenamiento por selección.
        selection_time = measure_sort(
            ordenar_seleccion,
            dataset,
            lambda song: song.titulo
        )

        # Ordenamiento por inserción.
        insertion_time = measure_sort(
            ordenar_insercion,
            dataset,
            lambda song: song.titulo
        )

        print(f"Búsqueda lineal:       {linear_time:.8f} segundos")
        print(f"Búsqueda binaria:      {binary_time:.8f} segundos")
        print(f"Ordenamiento selección: {selection_time:.8f} segundos")
        print(f"Ordenamiento inserción: {insertion_time:.8f} segundos")


if __name__ == "__main__":
    main()
