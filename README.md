# SIA - Trabajo Final

## El caso estudiado

Se elige utilizar el siguiente dataset https://archive.ics.uci.edu/ml/datasets/mushroom para entrenar un árbol de decision para luego predecir si un hongo es venenoso o comestible, informando sus características fisionómicas.

## Cómo ejecutar

1. Instalar Python 3 y Pipenv
2. Ejecutar `pipenv install` para instalar dependencias.
3. Para iniciar el backend: `FLASK_APP=server.py FLASK_ENV=development pipenv run python -m flask run`.