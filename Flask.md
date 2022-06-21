# Instalacion de Flask

### Instalar VirtualEnv
Instalacion en Window
```
pip install virtualenv
```

sudo apt install python3-pip
### Crear un ambiente Virtual con la versión de python a utilizar

- Antes de ejecutar este comando descargar la version en la pagina [3.7](https://www.python.org/downloads/release/python-370/)

```
virtualenv venv python=python3.7
```
### Activar el entorno virtual
```
.\venv\Scripts\activate
```
En caso de ser un sistema operativo MAC o LINUX
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
Dentro de este rachivo se ingresa todas las carpetas o archivos que no se van a cargar en github
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
### Configurar correo y nombre en git
```
git config --list
```
incluir correo
```
git config --global user.email "py.andres.castao@gmail.com"


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

#Crear la primer ruta para el hola mundo

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
Ejecutamos la instrución de run y validamos que el cambio en el Debug mode: estea en ON
```
Flask run
```

# Ciclo de request y response

<details>

```py
from flask import Flask, request

#Crear una instancia de Flask con nombre de APP

app = Flask(__name__) 

#Crear la primer ruta para el hola mundo

#crear el decorador
@app.route('/')
#Crear la funcion de hola mundo
def hello():
    #Creamos una nueva variable que va tener el la ip que detectamos en la requet
    user_ip = request-
    return 'Hello World Flask'
```
</details>

Con el siguiente codigo se crea un response que envia la informacion a una cookies y esta su vez es recibida por otra aplicación

<details>

```py
from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

todos = ['TODO 1', 'TODO 2', 'TODO 3']


@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)

    return response


@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    context = {
        'user_ip': user_ip,
        'todos': todos,
    }

    return render_template('hello.html', **context)


```
</details>

# Creacion del Template

### Crear una carpeta con el nombre de template

```
mkdir template
```
### Crear un archivo con el nombre hello.html en la carpeta de template

si estas en el bash de git escribir el siguente comando
```
touch hello.html 
```
si esta en la terminal de powersheet escribir el siguiente comando
```
New-Item hell.html
```

### Codigo para conectar el template de holla.html

<details>

```py
from flask import Flask,request, make_response,redirect,render_template

#Crear una instancia de Flask con nombre de APP

app = Flask(__name__) 

#Crear la primer ruta para el holo mundo

#crear el decorador
@app.route('/')
#Crear la funcion de hola mundo
def index():
    user_ip = request.remote_addr
    response=make_response(redirect('/hello'))
    response.set_cookie('user_ip',user_ip)
    return response


@app.route('/hello')
def hello():
    user_ip=request.cookies.get('user_ip')
     #Creamos una nueva variable que va tener el la ip que detectamos en la requet
    return render_template('hello.html', user_ip=user_ip)

```
</details>

### Escribir el siguientes codigo html en el arvhivo Hello.html

```html
<h1>Hello Wold Platzi, ti IP es{{user_ip}}</h1>
```

# Generar Estructuras de control

[Curso flash](https://docs.google.com/presentation/d/18WoO6bmYvlYVb6EmdanLOigjl9dmeUXpiuTUiaxLsKQ/edit#slide=id.g13588a5d876_0_0)

```html
{% if user_ip % }   

<h1>Hello Wold Platzi, ti IP es{{user_ip}}</h1>

{% else %}

<a href="{{ url_for('index') }}">Ir a inicio</a>

{% end if %}

```
### Crear una lista 
<details>

```py
from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

# Creamos una lista
todos = ['TODO 1', 'TODO 2', 'TODO 3']


@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)

    return response


@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')

    #Creamos unos parametros para ingresar una liste da aqui en adelante
    context = {
        'user_ip': user_ip,
        'todos': todos,
    }

    return render_template('hello.html', **context) # con la variable ** nos permite recorrer la lista total

```
</details>

En el html ingresamos el siguiente código
<details>

```html
<ul>
    {% for todo in todos %}
        <li>todo</li>
    {% endfor %}
</ul>

```
</details>

# Herencias en templates

[Jinja2 Snippet Extension](https://github.com/wyattferguson/jinja2-kit-vscode)

### Creamos un nuevo archivo llamado Base

```
touch base.html
```
### Incluir el código base
```html
<!DOCTYPE html>)
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>
```
</detarils>

>Apartir de este momento tenemos un power point con los print de pantalla

### Extender

Extender desde el archivo de hello.html la informacion de hello.html a base, escribiendo la siguente sentencia.
```
{% extends 'base.html' %}
```
#### Extender blokes anidados

Se coloca el siguiente código en el archivo base.

```html
{% block title %}
        Flask de Prueba |
    {% endblock title %}
```
Se coloca el siguiente código en el archivo hello.
```
{% block title %}
    {{super()}}
    Bienvenidos
{% endblock title %}
```
se valida la pestaña en el navegador la cual anida la informacion del "super" con la info del hijo "hello|base" -> "Bienvenidos|Flask de prueba"
### Extender contenido

Para extender contenido colocamos en el body del archivo base.html el siguiente codigo.

```
{% block content %}
    {% endblock %}
```
y en el archivo hello.html el siguiente código conteniendo la la informacion del contenido.
```html
{% block content  %}

{% if user_ip %}   
    <h1>Hello Wold Platzi, ti IP es {{user_ip}}</h1>
{% else %}
    <a href="{{ url_for('index') }}">Ir a inicio</a>
{% endif %}

<ul>
    {% for todo in todos %}
        <li>todo</li>
    {% endfor %}
</ul  

{% endblock  %}
```
### Crear una lista personalizada

Para personlizar los nombres tenemos que nombrarlos y adicional vincular la variable "todos" a la lista del contenido del archivo hello.html.

```py
todos = [
    'Comprar cafe', 
    'Enviar una solicitud de compra', 
    'Entregar video a producción']
```
y vincular la varible todos del archivo hello.html
```html
<ul>
    {% for todo in todos %}
        <li>{{todo}}</li>
    {% endfor %}
</ul  

```
## Creacion de Macros

Crear un archivo que se llamara macros.html
```
touch macros.html
```
En este archivo ingresar el siguiente código
```html
{% macro render_todo(todo) %}
<li>Descripción:{{todo}}</li>
{% endmacro %}
```
En el archivo de base.html importar el archivo de macro.html del objeto macro con la finalidad de que sea reconocido por el archivo hello.html

```html
{% import 'macros.html' as macros %}
```
En la lista del archivo hell.html incluir el objeto creado.

```html
<ul>
    {% for todo in todos %}
        {{macros.render_todo(todo)}}
    {% endfor %}
</ul 
```
# include y links

### Crear archvo navbar.html
con el siguiente comando
```
touch navbar.html
```

