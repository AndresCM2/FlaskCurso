# Instalación de Flask

<details>

### Instalar VirtualEnv

Instalaciones en Window
```
pip install virtualenv
```

### Crear un ambiente Virtual con la versión de python a utilizar

- Antes de ejecutar este comando descargar la version en la pagina [3.7](https://www.python.org/downloads/release/python-370/)

En caso tal de tener una version diferente de python ejecutar los siguientes comandos
```
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.7 1
```
```
virtualenv venv python=pytnon3.7
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


### Instalar un archivo requirement.txt

```
$ pip install -r requirements.tx
```
</details>

# Configurar Git

<details>

### Ingresar a git
```
git init
```
### Crear una archivo .gitingnore
```
touch .gitignore
```
Dentro de este archivo se ingresa todas las carpetas o archivos que no se van a cargar en github
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
### Jalar la conexión del repositorio Github
```
git pull origin main 
```
### Forzar
```
git pull origin main --allow-unrelated-histories
```
### Empujar información
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
```

</details>

# Crear una crear un clave privada

<details>

Validamos con el siguiente comando, que el correo y el nombre de usuario estén creados.
```
git config --global user.email "xxxxxxx@xxxxx.com"
```
Del mismo modo con la siguiente instrucción creamos el nombre del usuario.
```
git config --global user.name "Nxxxxxxxx Nxxxxxxxxx"
```
Con el siguiente comando validamos que efectivamente esten creados.

```
git config --global -l 
```
Después de validar que efectivamente fue creado el correo y el usuario, se procede a crear la clave ssh con el siguiente comando.
```
ssh-keygen -t rsa -b 4096 -C "xxxxxxxx@xxxxxx.com"
```
al ejecutar este comando me solicita crear el nombre del archivo le doy enter.
me solicita la clave con la que voy a guardar el nombre del archivo y me pide confirmarla nuevamente de esta forma me genera en la ruta de mi usuario una carpeta .ssh con en nombre id_rsa y otra con el nombre id_rsa.pub.

Con el siguiente comando validamos que efectivamente fue creado la clave privada.

```
eval "$(ssh-agent -s)"
```

de esta forma copio mi archivo.pub en la siguiente ruta en github.

Ingresamos a setting de github, luego a SSH and GPG keys, le damos click a New SSH key pegamos  la clave en Key, le damos y un title y luego lo add (añadimos).

Posterior a esto con el siguiente comando validamos la ruta.
```
git remote -v
```
vamos a github y copiamos en el enlace ssh generado para ejecutarlo en con el siguiente comando.
```
git remote set-url origin git@github.com:AndresCM2/FlaskCurso.git
```
Ejecutamos el siguiente comando el cual no va a solicita la clave personal que le asignamos.
```
git pull origin main --allow-unrelated-histories
```
Nos solicita confirmar.
```
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
```
y posterior nos pide la clave que le asignamos
```
Warning: Permanently added 'github.com' (ED25519) to the list of known hosts.
Enter passphrase for key '/c/Users/CMI/.ssh/id_rsa':xxxx
```

</details>


# Crear Archivo main.py

<details>

```
touch main.py
``` 
>main.py

En el archivo de main importar la librería de flask
```py
from flask import Flask

#Crear una instancia de Flask con nombre de APP

app = Flask(__name__) 

#Crear la primer ruta para el hola mundo

#crear el decorador
@app.route('/')
#Crear la función de hola mundo
def hello():
    return 'Hello World Flask'
```
</details>

# Prender un nuevo servidor para correr la aplicación en el navegador

<details>

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
</details>

# Debugging en Flask

<details>

Con la creación de un Servido para desarrollo con el método anterior siempre se requerirá correr nuevamente los cambios para que se logren visualizar en el navegador.

por lo tanto si activamos el Debug mode: con el comando
```
export FLASK_DEBUG=1
```
Validamos que esta variable exista
```
echo $FLASK_DEBUG
```
Ejecutamos la instrucción de run y validamos que el cambio en el Debug mode: este en ON
```
Flask run
```
</details>

# Ciclo de request y response

<details>

## Code


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

Con el siguiente codigo se crea un response que envia la informacion a una cookies y esta su vez es recibida por otra aplicación


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

<details>

### Crear una carpeta con el nombre de template

```
mkdir template
```
### Crear un archivo con el nombre hello.html en la carpeta de template

si estas en el bash de git escribir el siguiente comando
```
touch hello.html 
```
si esta en la terminal de powersheet escribir el siguiente comando
```
New-Item hell.html
```

### Código para conectar el template de hello.html


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


### Escribir el siguientes codigo html en el arvhivo Hello.html

```html
<h1>Hello Wold Platzi, ti IP es{{user_ip}}</h1>
```
</details>

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

```html
<ul>
    {% for todo in todos %}
        <li>todo</li>
    {% endfor %}
</ul>

```

</details>

# Herencias en templates

<details>

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

>Apartir de este momento tenemos un power point con los print de pantalla


### Extender

Extender desde el archivo de hello.html la información de hello.html a base, escribiendo la siguiente sentencia.
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
se valida la pestaña en el navegador la cual anida la información del "super" con la info del hijo "hello|base" -> "Bienvenidos|Flask de prueba"

### Extender contenido

Para extender contenido colocamos en el body del archivo base.html el siguiente código.

```
{% block content %}
    {% endblock %}
```
y en el archivo hello.html el siguiente código conteniendo la la información del contenido.
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

Para personalizar los nombres tenemos que nombrarlos y adicional vincular la variable "todos" a la lista del contenido del archivo hello.html.

```py
todos = [
    'Comprar cafe', 
    'Enviar una solicitud de compra', 
    'Entregar video a producción']
```
y vincular la variable todos del archivo hello.html
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

</details>


# include y links

### Crear arch$ivo navbar.html
con el siguiente comando
```
touch navbar.html
```

>>>>>>> 45b7ec1cc661bd7b6034b65a3490f6d67232f23c
