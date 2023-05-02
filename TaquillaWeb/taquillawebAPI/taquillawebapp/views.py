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
            #return JsonResponse(data)
            return JsonResponse(data, safe = False, json_dumps_params = {'ensure_ascii':False})

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
            #return JsonResponse(data)
            return JsonResponse(data, safe = False, json_dumps_params = {'ensure_ascii':False})
            #pass
        else:
            return HttpResponse("Contraseña incorrecta", status=401)
    
    # Si el método no es POST:  
    return HttpResponseBadRequest()

#---------------- Endpoint 3 (GET /cines): conseguir información de todos los cines. ----------------#
@csrf_exempt
def cines_view(request):
    if request.method == 'GET':
        # Obtener el valor de la cabecera "Authorization"
        authorization_header = request.META.get('HTTP_AUTHORIZATION')

        try:  # si el token es diferente a los tokens que hay en la BD el usuario no está introduciento el token correcto
            usuario = Tusuarios.objects.get(token = authorization_header)
            
        except Tusuarios.DoesNotExist:
            return HttpResponse("La autenticación ha fallado.", status=400)

        listacines = Tcines.objects.all() #consultamos la base de datos
        respuesta_final=[] # creamos una lista Python vacía

        # Creo un diccionario (un diccionario es como un Json) con las sesiones y lo añado a respuesta_final (a mayores)
        sesionescines = {
            "Sesiones para todos los cines": {
                "Sesión 1": "16:30h - 18:30h", "Sesión 2": "19:00h - 21:00h", "Sesión 3":"21:30h - 23:30h"
            }
        }
        
        respuesta_final.append(sesionescines)

        for instanciacine in listacines: # Recorremos con un for los resultados de la consulta anterior
            diccionario = {} # creamos un diccionario Python vacío 
            diccionario['id_cine'] = instanciacine.id  
            diccionario['nombre_cine'] = instanciacine.cinenombre
            diccionario['logo_cine'] = instanciacine.cinelogo
            diccionario['cantidadsalas_cine'] = instanciacine.cantidadsalas
            respuesta_final.append(diccionario) # Añadimos un diccionario Python a la lista Python por cada iteración

        #return JsonResponse(respuesta_final, safe=False)
        return JsonResponse(respuesta_final, safe = False, json_dumps_params = {'ensure_ascii':False})
    
    # Si el método no es GET:  
    return HttpResponseBadRequest()

#---------------- Endpoint 4 (GET /peliculas): conseguir información de todas las peliculas. ----------------#
@csrf_exempt
def peliculas_view(request):
    if request.method == 'GET':
        # Obtener el valor de la cabecera "Authorization"
        authorization_header = request.META.get('HTTP_AUTHORIZATION')

        try:  # si el token es diferente a los tokens que hay en la BD el usuario no está introduciento el token correcto
            usuario = Tusuarios.objects.get(token = authorization_header)
            
        except Tusuarios.DoesNotExist:
            return HttpResponse("La autenticación ha fallado.", status=400)

        listapeliculas = Tpeliculas.objects.all() # consultamos la base de datos
        respuesta_final=[] # creamos una lista Python vacía, será una lista de diccionarios

        for instanciapelicula in listapeliculas: # Recorremos con un for los resultados de la consulta anterior
            diccionario = {} # creamos un diccionario Python vacío 
            diccionario['id_pelicula'] = instanciapelicula.id  
            diccionario['titulo_pelicula'] = instanciapelicula.titulo
            diccionario['estreno_pelicula'] = instanciapelicula.estreno
            diccionario['sinopsis_pelicula'] = instanciapelicula.sinopsis
            diccionario['precio_pelicula'] = instanciapelicula.peliculaprecio
            diccionario['cartel_pelicula'] = instanciapelicula.cartel

            respuesta_final.append(diccionario) # Añadimos un diccionario Python a la lista Python por cada iteración

        #return JsonResponse(respuesta_final, safe=False)
        return JsonResponse(respuesta_final, safe = False, json_dumps_params = {'ensure_ascii':False})

    
    # Si el método no es GET:  
    return HttpResponseBadRequest()


#---------------- Endpoint 5 (GET /peliculas/<id>): conseguir información la pelicula con el id introducido. ----------------#
@csrf_exempt
def pelicula_por_id_view(request, id_solicitado):
    if request.method == 'GET':
        # Obtener el valor de la cabecera "Authorization"
        authorization_header = request.META.get('HTTP_AUTHORIZATION')

        try:  # si el token es diferente a los tokens que hay en la BD el usuario no está introduciento el token correcto
            usuario = Tusuarios.objects.get(token = authorization_header)
            
        except Tusuarios.DoesNotExist:
            return HttpResponse("La autenticación ha fallado.", status=400)

        pelicula_solicitada = Tpeliculas.objects.get(id = id_solicitado) # consultamos la base de datos
        
        respuesta = {
            "id_pelicula": pelicula_solicitada.id,
            "titulo_pelicula": pelicula_solicitada.titulo,
            "estreno_pelicula": pelicula_solicitada.estreno,
            "sinopsis_pelicula": pelicula_solicitada.sinopsis,
            "precio_pelicula": pelicula_solicitada.peliculaprecio,
            "cartel_pelicula": pelicula_solicitada.cartel
        }

        return JsonResponse(respuesta, safe = False, json_dumps_params = {'ensure_ascii':False})
    
    # Si el método no es GET:  
    return HttpResponseBadRequest()


    #------------ Endpoint 6 (GET /cine/<id>/peliculas): conseguir información las peliculas del cine cuyo id es el introducido. ------------#
    #------------ FUNCIONA_01 ------------#
@csrf_exempt
def peliculas_por_cine_view(request, id_cine_solicitado):
    if request.method == 'GET':
        # Obtener el valor de la cabecera "Authorization"
        authorization_header = request.META.get('HTTP_AUTHORIZATION')

        try:  # si el token es diferente a los tokens que hay en la BD el usuario no está introduciento el token correcto
            usuario = Tusuarios.objects.get(token = authorization_header)
            
        except Tusuarios.DoesNotExist:
            return HttpResponse("La autenticación ha fallado.", status=400)
        
        cine_solicitado = Tcines.objects.get(id = id_cine_solicitado) # consultamos la base de datos
        salas_cine_solicitado = Tsalas.objects.filter(id_cine = id_cine_solicitado) # get solo devuelve un valor

        # para cada sala obtener la pelicula que proyecta y meterla en una lista
        lista_peliculas=[] # creamos una lista Python vacía

        for instanciasala in salas_cine_solicitado: # Recorremos con un for los resultados de la consulta anterior
            pelicula = instanciasala.id_pelicula  
            # chat GPT: Cuando se accede a un campo de clave foránea en un objeto Python a través de la notación punto, 
            # lo que se devuelve es el objeto relacionado al que apunta la clave foránea.

            lista_peliculas.append(pelicula) # Añadimos a la lista Python por cada iteración

        # return HttpResponse(lista_peliculas) # hasta aquí funciona

        respuesta_final=[] # creamos una lista Python vacía, será una lista de diccionarios

        # Creo un diccionario (un diccionario es como un Json) con el nombre del cine y num salas y lo añado a respuesta_final (a mayores)
        datoscine = {'Cine solicitado:': cine_solicitado.cinenombre, 'Número de salas:': cine_solicitado.cantidadsalas}
        
        respuesta_final.append(datoscine)

        for pelicula in lista_peliculas:

            diccionario = {} # creamos un diccionario Python vacío 
            diccionario['id_pelicula'] = pelicula.id  
            diccionario['titulo_pelicula'] = pelicula.titulo
            diccionario['estreno_pelicula'] = pelicula.estreno
            diccionario['sinopsis_pelicula'] = pelicula.sinopsis
            diccionario['precio_pelicula'] = pelicula.peliculaprecio
            diccionario['cartel_pelicula'] = pelicula.cartel

            respuesta_final.append(diccionario) # Añadimos un diccionario Python a la lista Python por cada iteración

        return JsonResponse(respuesta_final, safe = False, json_dumps_params = {'ensure_ascii':False})
    
    # Si el método no es GET:  
    return HttpResponseBadRequest()


    #------------ Endpoint 7 (GET /peliculas/estrenos): obtener las películas que son estrenos. ------------#
@csrf_exempt
def peliculas_estrenos(request):
    if request.method == 'GET':
        # Obtener el valor de la cabecera "Authorization"
        authorization_header = request.META.get('HTTP_AUTHORIZATION')

        try:  # si el token es diferente a los tokens que hay en la BD el usuario no está introduciento el token correcto
            usuario = Tusuarios.objects.get(token = authorization_header)
            
        except Tusuarios.DoesNotExist:
            return HttpResponse("La autenticación ha fallado.", status=400)
        
        estrenos = Tpeliculas.objects.filter(estreno = 1)

        cantidad_estrenos = len(estrenos)

        respuesta_final_estrenos=[]

        # Creo un diccionario (un diccionario es como un Json) y lo añado a respuesta_final (a mayores)
        datosextra = {'Número total de películas en estreno:': cantidad_estrenos}

        respuesta_final_estrenos.append(datosextra)

        for pelicula_estreno in estrenos:

            diccionario = {} # creamos un diccionario Python vacío 
            diccionario['id_pelicula'] = pelicula_estreno.id  
            diccionario['titulo_pelicula'] = pelicula_estreno.titulo
            diccionario['estreno_pelicula'] = pelicula_estreno.estreno
            diccionario['sinopsis_pelicula'] = pelicula_estreno.sinopsis
            diccionario['precio_pelicula'] = pelicula_estreno.peliculaprecio
            diccionario['cartel_pelicula'] = pelicula_estreno.cartel

            respuesta_final_estrenos.append(diccionario) # Añadimos un diccionario Python a la lista Python por cada iteración

        return JsonResponse(respuesta_final_estrenos, safe = False, json_dumps_params = {'ensure_ascii':False})
    
    # Si el método no es GET:  
    return HttpResponseBadRequest()
