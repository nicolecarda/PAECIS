import os
import pickle
from statistics import LinearRegression # necesitamos también importar las librerías acá
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.discriminant_analysis import StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor

def normalizar_pd(data):

    data = pd.read_excel(f'archivos\df_limpio.xlsx')

    # lo mismo de antes
    columns_to_normalize = ['Año', 'Egresos', 'Día-cama disponible', 'Promedio de permanencia']

    # Z-score
    scaler = StandardScaler() # instanciamos el objeto que escala
    data[columns_to_normalize] = scaler.fit_transform(data[columns_to_normalize]) # fit_transform: primero se "amolda" (fitea), después aplica la transformacion sobre las columnas a normalizar
    
    print("Normalización lista.")
    return data


def normalizarDos_pd(data):

    data = pd.read_excel(f'archivos\df_internacion_mh.xlsx')

    # lo mismo de antes
    columns_to_normalize = ['SERVICIO', 'INGRESOS', 'ALTAS', 'DIAS_CAMAS_DISPONIBLES', 'PROMEDIO_PERMANENCIA', 'GIRO_CAMA', 'NOMBRE_EFECTOR_BADATA']

    # Z-score
    scaler = StandardScaler() # instanciamos el objeto que escala
    data[columns_to_normalize] = scaler.fit_transform(data[columns_to_normalize]) # fit_transform: primero se "amolda" (fitea), después aplica la transformacion sobre las columnas a normalizar
    
    print("Normalización lista.")
    return data




def entrenar_modelo(data, modelo='LinearRegression', persistir=False):
   
    data = pd.read_excel(f'archivos\df_limpio.xlsx')

    target = data['Promedio de permanencia']
    features = data[['Año', 'Egresos', 'Día-cama disponible']]

    # Dividir en train y test
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

    # Seleccionar el modelo según el parámetro 'modelo'
    if modelo == 'LinearRegression':
        model = LinearRegression()
    elif modelo == 'DecisionTree':
        model = DecisionTreeRegressor(random_state=42)
    else:
        raise ValueError(f"Modelo no soportado: {modelo}")

    # Entrenar el modelo
    model.fit(X_train, y_train)

    # Realizar predicciones sobre los datos de prueba
    y_pred = model.predict(X_test)

    # Evaluación del modelo
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    # Imprimir resultados
    print(f'Entrenamiento completo.')
    print(f'El modelo tuvo un MSE de {mse}.')
    print(f'El modelo tuvo un R2 de {r2}.')

    # Si se requiere persistir el modelo
    if persistir:
        # Crear la carpeta 'models' si no existe
        output_dir = 'models'
        os.makedirs(output_dir, exist_ok=True)

        # Obtener el nombre del algoritmo
        nombre_algoritmo = type(model).__name__

        # Construir el camino completo del archivo
        path_modelo = f'{output_dir}/{nombre_algoritmo}.pkl'

        # Guardar el modelo serializado en el archivo
        with open(path_modelo, 'wb') as archivo:
            pickle.dump(model, archivo)
            print(f'El modelo fue guardado en {path_modelo}')

    # Devolver el modelo entrenado si no se persiste
    return model


def entrenar_modeloDos(data, modelo='DecisionTree', persistir=False):
   
    data = pd.read_excel(f'archivos\df_internacion_mh.xlsx')

    target = data['PROMEDIO_PERMANENCIA']
    features = data[['SERVICIO', 'INGRESOS', 'ALTAS', 'DIAS_CAMAS_DISPONIBLES', 'GIRO_CAMA', 'NOMBRE_EFECTOR_BADATA']]

    # Dividir en train y test
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

    # Seleccionar el modelo según el parámetro 'modelo'
    if modelo == 'LinearRegression':
        model = LinearRegression()
    elif modelo == 'DecisionTree':
        model = DecisionTreeRegressor(random_state=42)
    else:
        raise ValueError(f"Modelo no soportado: {modelo}")

    # Entrenar el modelo
    model.fit(X_train, y_train)

    # Realizar predicciones sobre los datos de prueba
    y_pred = model.predict(X_test)

    # Evaluación del modelo
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    # Imprimir resultados
    print(f'Entrenamiento completo.')
    print(f'El modelo tuvo un MSE de {mse}.')
    print(f'El modelo tuvo un R2 de {r2}.')

    # Si se requiere persistir el modelo
    if persistir:
        # Crear la carpeta 'models' si no existe
        output_dir = 'models'
        os.makedirs(output_dir, exist_ok=True)

        # Obtener el nombre del algoritmo
        nombre_algoritmo = type(model).__name__

        # Construir el camino completo del archivo
        path_modelo = f'{output_dir}/{nombre_algoritmo}.pkl'

        # Guardar el modelo serializado en el archivo
        with open(path_modelo, 'wb') as archivo:
            pickle.dump(model, archivo)
            print(f'El modelo fue guardado en {path_modelo}')

    # Devolver el modelo entrenado si no se persiste
    return model
