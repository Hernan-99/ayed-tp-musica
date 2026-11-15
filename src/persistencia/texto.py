from pathlib import Path

from src.excepciones import ArchivoInvalidoError


def cargar_texto(ruta):
    """Carga secuencial de un .txt: un registro por línea, separado por coma.
    Devuelve una lista de dicts (E1 puede quedar así)."""

    ruta = Path(ruta)

    if not ruta.is_file():
        raise FileNotFoundError("El archivo no existe.")

    rows = []
    try:
        with ruta.open('r', encoding='utf-8-sig') as f: # file
            headers = f.readline().strip().split(",")

            if not headers or headers == ['']:
                raise ArchivoInvalidoError("El archivo no tiene encabezados.")

            for line_number, line in enumerate(f, start=2):
                line = line.strip()

                if not line:
                    continue

                values = line.split(",")
                if len(values) != len(headers):
                    raise ArchivoInvalidoError(
                        f"La línea {line_number}: se esperan "
                        f"{len(headers)} campos, pero se encontraron "
                        f"{len(values)}.")

                rows.append(dict(zip(headers, values)))
    except (OSError, UnicodeError) as error:
        raise ArchivoInvalidoError(
            f"No se pudo leer el archivo: {ruta}"
        ) from error

    return rows


def guardar_texto(ruta, filas, encabezados):
    """Escribe el catálogo en .txt con la primera línea de encabezados."""
    route = Path(ruta)

    try:
        with route.open("w", encoding="utf-8-sig") as f: #file
            f.write(",".join(encabezados) + "\n")

            for row in filas:
                values = []
                for header in encabezados:
                    value = str(row[header])
                    if "," in value or "\n" in value or "\r" in value:
                        raise ArchivoInvalidoError(
                            f"Valor incompatible con el formato: {value}"
                        )
                    values.append(value)
                f.write(",".join(values) + "\n")
    except (OSError, UnicodeError, KeyError) as error:
        raise ArchivoInvalidoError(
            f"No se pudo guardar el archivo: {route}"
        ) from error
