# API con Flask

Lo primero que hice fue crear un proyecto e inicializar un entorno venv con el comando **python -m virtualenv venv**

En las carpetas se usa lo siguiente:
- *Database* se usa para los archivos de conexión a la base de datos.
- *Models* Se usa para crear las entidades que maneja la API
- *Routes* Es el controlador que contiene y gestiona todas las rutas y métodos HTTP
- *utils* Carpeta de utilidades, como por ejemplo, funciones especiales que no quiero crear siempre, como un formateador de fechas.
- *.env* Es una archivo de configuración general.


## Segundo paso

Ahora iniciamos en yendo a venv/Scripts/activate

## Lista de paquetes PIP
- pip install flask flask-cors psycopg2 python-decouple python-dotenv

# Archivo app.py
En este archivo lo primero que hicimos fue definir un método para retornar una respuesta ante todos los 404.

Luego, en el if __name__ == '__main__': lo que hicimos fue declarar algunas cosas importante como por ejemplo:

- Blueprints: Estos son las URLs principales para cada controlador.

- Error handlers: Estos son manejadores de errores. Aquí decimos que a los 404 les retornamos cierto método.

# Archivos de entidades
Los archivos de entidades tienen un main para definir sus rutas. Por ejemplo: @app.route o @movie.route

Aquí definimos los procesos que podemos hacer con esa entidad.

## Dato importante sobre __init__.py
En la carpeta routes incluímos ese archivo, no tiene nada pero se usa para que reconozca la carpeta como un módulo y podamos acceder a ella fácilmente.
