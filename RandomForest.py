import click
import pandas as pd
from utils import normalizarDos_pd, entrenar_modeloDos  # Asegúrate de importar las funciones necesarias
 

@click.command()
@click.option('--path', type=click.Path(exists=True), required=True, help="Ruta hacia la carpeta donde están los CSVs.")
@click.option('--persistir', is_flag = True, help="Opcional: permite persistir el modelo creado.")


def main(path, persistir):
   
    file_path = f'{path}/df_internacion_mh.xlsx'

    # Normalizar los datos
    df_normalizado = normalizarDos_pd(file_path)

    # Entrenar el modelo
    entrenar_modeloDos(df_normalizado, persistir=persistir)

    # Mensaje de confirmación
    click.echo('Proceso completo.')

if __name__ == "__main__":
    main()