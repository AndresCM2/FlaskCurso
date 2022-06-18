# Instalacion de Flask

### Instalar VirtualEnv
```
pip install virtualenv
```

### Crear un ambiente Virtual con la versión de python a utilizar

- Antes de ejecutar este comando descargar la version en la pagina [3.7](https://www.python.org/downloads/release/python-370/)

```
virtualenv venv python=pytnon3.7
```
### Activar el entorno virtual
```
.\venv\Scripts\activate
```
- en caso de ser un sistema operativo MAC o LINUX
```
Source venv/Scripts/activate
```

### Instalar Flask
```
pip install flask
```

### Validar la instalacion de Flask

```
pip freeze 
```
### Crear archivo requirements.txt

```
pip freeze > requirements.txt
```

# Configurar Git

### Ingresar a git
```
git init
```
### Crear una archivo .gitingnore
```
touch .gitignore
```
dentro de este rachivo se ingresa todas las carpetas o archivos que no se van a cargar en github
### Cambiar de rama a main
```
git branch -M main
```
### Conectar con github
```
git remote add origin https://github.com/AndresCM2/FlaskCurso.git
```
### validar las nombre
```
git remote
```
### Validar rutas
```
git remote -v
```
### Jalar la coneccion del repositori Github
```
git pull origin main 
```
### Forzar
```
git pull origin main --allow-unrelated-histories
```
### Enpujar informacion
```
git push origin main
```

# Crear Archivo main.py
```
touch main.py
``` 
En el archivo de main importar la libreria de flask

>`main.py`
<details>  

```py
from flask import Flask

#Crear una instancia de Flask con nombre de APP

app = Flask(__name__) 

#Crear la primer ruta para el holo mundo

#crear el decorador
@app.route('/')
#Crear la funcion de hola mundo
def hello():
    return 'Hello World Flask'
```
</details>

# Prender un nuevo servidor para correr la aplicacion en el navegador

### Crear una variable de ambiente en el entorno de comandos
```
export FLASK_APP=main.py

```
### Validamos que la variable este creada

```
echo $FLASK_APP
```
### Ejecutar Flak run para prender nuestro servidor

```
Flask run
```
# Debugging en Flask

Con la creacion de un Servido para desarrollo con el metodo anterior siempre se requerira correr nuevamente los cambios para que se logren visualidar en el navegador.

por lo tanto si activamos el Debug mode: con el comando
```
export FLASK_DEBUG=1
```
Validamos que esta varible exista
```
echo $FLASK_DEBUG
```
Ejecutamos la insturcion de run y validamos que el cambio en el Debug mode: estea en ON
```
Flask run
```
# Ciclo de request y response
```py
from flask import Flask, request

#Crear una instancia de Flask con nombre de APP

app = Flask(__name__) 

#Crear la primer ruta para el holo mundo

#crear el decorador
@app.route('/')
#Crear la funcion de hola mundo
def hello():
    #Creamos una nueva variable que va tener el la ip que detectamos en la requet
    user_ip = request-
    return 'Hello World Flask'
```
