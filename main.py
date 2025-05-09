from flask import Flask, request, render_template, make_response


app = Flask (__name__)




@app.route("/")
def home ():
    return "PAGINA DE INICIO"

#Ruta para parametros URL
@app.route("/consulta")
def ruta_consulta():
    producto=request.args.get("product")
    talla=request.args.get("talla")
    if producto and talla is None:
        return f"Se esta consultando solo el producto {producto}"
    if talla is None and producto :
        return f"Por favor ingrese el producto a buscar {talla}"
    if talla is None and producto is None:
        return f"Bienvenido a la pagina de ropa"
    return f"Se esta consultando el producto {producto} y la talla {talla}"

#Ruta para capturar datos por el cuerpo de solicitud para el body
listado=[]
@app.route("/registro", methods=["GET"])
def ruta_registro():
    #listado=[{"nombre": "Lewin", "email":"lewindcg@gmail.com"}]
    return render_template("formulario.html", listado=listado)

@app.route("/registro", methods=["POST"])
def procesar_registro():

    nombre=request.form.get("nombre")
    correo=request.form.get("correo")
    estudiantes={"nombre":nombre, "correo":correo}
    listado.append(estudiantes)
    #print (nombre)
    return f"El estudiante a registrar es {nombre} y el correo a registrar es {correo}"

#PARAMETROS EN LA RUTA

@app.route("/estudiantes/<string:area>/<int:grupo>")
def mostrar_estudiantes(area, grupo):
    return f"El programa de formacion consultado es {area} y el grupo consultado es {grupo}"

#SOLICITUD TIPO 4 ENCABEZADOS 
@app.route("/ver-headers")
def ver_headers():
    agente_usuario = request.headers.get('User-Agent')
    return f"Tu navegador es: {agente_usuario}"

#GESTION DE LAS COOKIES
@app.route('/crear-cookie')
def crear_cookie():
    respuesta = make_response("Cookie creada!")#ES UN MENSAJE EN NAVEGADOR
    respuesta.set_cookie('usuario_logueado', 'true', max_age=60*60*24, httponly=True)
    return respuesta

@app.route('/leer-cookie')
def leer_cookie():
    valor = request.cookies.get('usuario_logueado')
    return f"Valor de la cookie: {valor}"

if __name__ == "__main__": 
    app.run(debug=True)