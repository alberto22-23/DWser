import json  # La función json.loads es parte del módulo json de Python
from sqlite3 import IntegrityError

# La biblioteca estándar de Django se localiza en el paquete django.contrib.
from django.contrib.auth import authenticate, login

# Importaciones para el ejercicio:
from django.views.decorators.csrf import csrf_exempt
from .models import * #Importo todos los modelos
from django.contrib.auth.hashers import check_password # para comprobar contraseña
import jwt # para generar token

from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse, StreamingHttpResponse
from django.shortcuts import render

# Create your views here.

def pagina_de_prueba(request):
    return HttpResponse("<h1>Bienvenid@ a la página de prueba</h1>")

#---------------- Endpoint 1 (POST /users): creación de un nuevo usuario. ----------------#

@csrf_exempt
def nuevousuario_view(request):
    json_request = json.loads(request.body)
    if request.method == 'POST':
        # Declaramos los campos que se van a añadir a la BD
        pusuarionombre = json_request['usuarioNombre']
        ppassword = json_request['password']
        pemail = json_request['email']

        # a) Comprobamos que se han cubierto todos los campos
        if not all([pusuarionombre, ppassword, pemail]):
            return HttpResponse("Hay campos sin cubrir", status=400)
        # HttpResponse pág. 586

        # b) Comprobamos que no existe un usuario con el mismo correo
        # 1er email es el campo de la bd, el 2º es el email del request
        if Tusuarios.objects.filter(email=pemail).exists():
            return HttpResponse("El email ya exite", status=400)

        # Si todo funciona se crea el usuario si no devolvemos error
        try:
            # Puedes crear usuarios con el método create_user() pag. 304. Crea pero no guarda un objeto usuario en un simple paso
            #nuevo_usuario = Tusuarios.objects.create_user(pusuarionombre, ppassword, pemail)
            #nuevo_usuario.set_password(ppassword) 
            # Este método set_password() está definido en el modelo (clase) Tusuarios, encripta la contraseña
            #nuevo_usuario.save() # Guarda el nuevo usuario en la base de datos
            # data = {
                #"status": "Se ha creado el nuevo usuario.",
                #"data": {
                    #"usuarioNombre": pusuarionombre,
                    #"password": ppassword,
                    #"email": pemail
                #}
            #}
            #return JsonResponse(data)
            nuevo_usuario = Tusuarios()
            nuevo_usuario.usuarionombre = pusuarionombre
            nuevo_usuario.password = ppassword
            nuevo_usuario.set_password(ppassword) 
            # Este método set_password() está definido en el modelo (clase) Tusuarios, encripta la contraseña
            nuevo_usuario.email = pemail
            nuevo_usuario.save() # Guarda el nuevo usuario en la base de datos
            #return HttpResponse("Se ha creado el nuevo usuario.", status=201)
            nombre = nuevo_usuario.usuarionombre
            data = {
                "status": "Se ha creado el nuevo usuario, status=201",
                "data": {
                    "nombre":nombre
                }
            }
            return JsonResponse(data)

        except IntegrityError:
            return HttpResponse(status=409)
    
    # Si el método no es POST:
    return HttpResponseBadRequest()


#---------------- Endpoint 2 (POST /sessions): login de usuario. ----------------#
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        # recogemos el cuerpo de la petición
        json_request = json.loads(request.body)
        # En Django, json.loads es una función que se utiliza para convertir una cadena JSON (JavaScript Object Notation) en un objeto de Python
        
        pusuarionombre = json_request['usuarioNombre'] # cogemos el nombre
        pemail = json_request['email']  # cogemos el email
        ppassword = json_request['password']  # cogemos la clave

        if not all([pusuarionombre, ppassword, pemail]):  # si no están todos los campos, error del cliente
            return HttpResponse("Hay campos sin cubrir", status=400)

        try:  # si el email es diferente a los emails que hay en la BD el usuario no existe
            usuario = Tusuarios.objects.get(email=pemail)
            
        except Tusuarios.DoesNotExist:
            return HttpResponse("El email no está registrado", status=400)
        
        # Validamos la contraseña (no definimos el método check_password() en el modelo (clase) Tusuarios, lo importamos)
        if check_password(ppassword, usuario.password):
		    # Generar un token de sesion:
            payload = {
	            'usuario_id': usuario.id, #son los atributos de la clase Tusuarios
	            'usuario_nombre': usuario.usuarionombre
            }
            secret = 'misecreto'
            token = jwt.encode(payload, secret, algorithm='HS256')
            print (token)
            # Metemos el token en la base de datos, en el campo token de Tusuarios para el usuario actual
            usuario.token = token
            usuario.save() # Guarda el valor del campo en el objeto usuario
            # Enviamos el token en la respuesta HTML al cliente
            data = {
                "status": "Inicio de sesión correcto, status=201",
                "data": {
                    "token":token
                }
            }
            return JsonResponse(data)
            #pass
        else:
            return HttpResponse("Contraseña incorrecta", status=401)
    
    # Si el método no es POST:  
    return HttpResponseBadRequest()
