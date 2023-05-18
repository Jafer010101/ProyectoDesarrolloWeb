# Importar el módulo Flask
from flask import Flask

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Definir una ruta para la página de inicio
@app.route('/')
def hello_world():
    return '¡Hola mundo!'

# Comprobar si el script se está ejecutando directamente y no importado como un módulo
if __name__ == '__main__':
    # Ejecutar la aplicación en el servidor local en el puerto 5000
    app.run()
