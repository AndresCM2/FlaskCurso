from flask import Flask, redirect, request, make_response

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
    return 'Hel World Fla . tu ip es {}'.format(user_ip)