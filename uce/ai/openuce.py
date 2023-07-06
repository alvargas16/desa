import openai
from pydantic import BaseModel

openai.organization = 'org-qlfeJ5qRmqdxY6Vi6lA8OI68'
openai.api_key = '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'


class Document(BaseModel):
    item: str = 'factorial de un numero'


def process_inference(user_prompt) -> str:
    print('[PROCESANDO]'.center(40, '-'))
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """Eres un profesor de programaciòn, nivel universitario, enseñas como programar
        E.G
        Calcular promedios de notas de los estudiantes
        CODIGO:
        # Importar librerías necesarias
    import numpy as np
    import pandas as pd

# Definir una función para calcular el promedio
    def calcular_promedio(notas):
    promedio = np.mean(notas)
    return promedio

# Leer archivo de notas
    notas = pd.read_csv('notas.csv')

# Calcular promedio de cada estudiante
    promedios = []
    for i in range(len(notas)):
    promedio = calcular_promedio(notas.iloc[i, 1:])
    promedios.append(promedio)

# Agregar columna de promedios al archivo de notas
    notas['Promedio'] = promedios

# Guardar archivo con los promedios
    notas.to_csv('notas_con_promedio.csv', index=False)
        ...
        """},
            {"role": "user", "content": user_prompt}
        ]
    )
    response = completion.choices[0].message.content
    return response
