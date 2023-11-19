#Importaciones de las clases 
from Username import *
from Post import *
from Like import *
from Comentario import *
from Estudiante import *
from Profesor import *

import requests
import json 
from datetime import date

###########################################################################################
#Acceso a api de usuarios

def apis_usuario(usuarios):
    info_usuarios = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-3/api-proyecto/08d4d2ce028692d71e9f8c32ea8c29ae24efe5b1/users.json")
    info_usuarios = info_usuarios.json()

    #Separar lista de diccionarios y appendearlos a la lista 
    for info in info_usuarios:
        user = ""
        
        if info["type"] == "professor":
            user = Profesor(info["id"], info["firstName"],info["lastName"],info["email"],info["username"],info["following"], "profesor", info["department"])
        else:
            user = Estudiante(info["id"],info["firstName"],info["lastName"],info["email"],info["username"],info["following"], "estudiante", info["major"])

        usuarios.append(user)

#Acceso a api de posts 
def apis_post(posts):
    info_publicacion = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-3/api-proyecto/main/posts.json")
    info_publicacion = info_publicacion.json()
#Separar lista de diccionarios y appendearlos a la lista 
    for info in info_publicacion:
        new = Post(info["publisher"],info["type"],info["multimedia"]["url"],info["caption"],info["tags"], info["date"])
        posts.append(new)

#guardado es el inverso de extraccion, pasamos los datos de objtos a diccionario y los dic los escribimos a los archivos .json()
def guardado_info(usuarios,posts,likes,comentarios):
    lista_usuarios_json = []
    for usuario in usuarios:
        if usuario.tipo == "estudiante":
            dic_usuario = {
                "id": usuario.id,
                "firstName": usuario.nombre,
                "lastName": usuario.apellido,
                "email": usuario.correo,
                "username": usuario.username,
                "type": usuario.tipo,
                "career": usuario.carrera,
                "following": usuario.following
            }
            lista_usuarios_json.append(dic_usuario)
        else:
            dic_usuario = {
                "id": usuario.id,
                "firstName": usuario.nombre,
                "lastName": usuario.apellido,
                "email": usuario.correo,
                "username": usuario.username,
                "type": usuario.tipo,
                "department": usuario.departamento,
                "following": usuario.following
            }
            lista_usuarios_json.append(dic_usuario)
    with open("usuario.json", "w") as file: # Guardar un archivo Json
        json.dump(lista_usuarios_json, file)
        file.close()
    lista_posts_json = []
    for post in posts:
        dic_post = {
        "publisher":  post.username,
        "type": post.tipo,
        "caption": post.caption,
        "date" : post.date,
        "tags" : post.hashtag,
        "url": post.url,
        "multimedia": {
            "type": post.tipo,
            "url" : post.url
        }
        
        }
        lista_posts_json.append(dic_post)
    with open("post.json", "w") as file: # Guardar un archivo Json
        json.dump(lista_posts_json, file)
        file.close()

        
    lista_likes_json = []
    for like in likes:
        dic_likes = {
            "Post": like.post,
            "Usuario": like.username
        }
        lista_likes_json.append(dic_likes)
    with open("likes.json", "w") as file: # Guardar un archivo Json
        json.dump(lista_likes_json, file)
        file.close()


    lista_comentarios_json = []
    for comentario in comentarios:
        dic_comentarios = {
            "Usuario": comentario.username,
            "Post": comentario.post,
            "Comentario": comentario.comentario,
            "Date": comentario.date
        }
        lista_comentarios_json.append(dic_comentarios)
        
    with open("comentarios.json", "w") as file: # Guardar un archivo Json
        json.dump(lista_comentarios_json, file)
        file.close()
    
def extraccion_info (usuarios,posts,likes,comentarios):
    with open("usuario.json", "r") as file: # abre el archivo lo lee y guarda su informacion en la variable info_usuarios
        info_usuarios = json.load(file)
        file.close()
    
    with open("post.json", "r") as file: # Guardar un archivo Json
        info_publicacion = json.load(file)
        file.close()

    with open("likes.json", "r") as file: # Guardar un archivo Json
        info3 = json.load(file)
        comentarios = info3
        file.close()

    with open("comentarios.json", "r") as file: # Guardar un archivo Json
        info4 = json.load(file)
        comentarios = info4
        file.close()
    

    
    # si es 0, no informacion en mis archivos asi que sacamos la informacion del apis entonces
    if len(info_usuarios) ==0:
        #llamar funciones de las apis - proceso de información 
        apis_usuario(usuarios)
    else:
#Separar lista de diccionarios y appendearlos a la lista 
        for info in info_usuarios:
            if info["type"] == "profesor":
                user = Profesor(info["id"], info["firstName"],info["lastName"],info["email"],info["username"],info["following"], "profesor", info["department"])
            else:
                user = Estudiante(info["id"],info["firstName"],info["lastName"],info["email"],info["username"],info["following"], "estudiante", info["career"])

            usuarios.append(user)
    
    if len(info_publicacion) ==0:
        #llamar funciones de las apis - proceso de información
        apis_post(posts)
    else:
        #Separar lista de diccionarios y appendearlos a la lista 
        for info in info_publicacion:
            new = Post(info["publisher"],info["type"],info["multimedia"]["url"],info["caption"],info["tags"], info["date"])
            posts.append(new)



#Esta es la funcion de menu, la cual será reutilizada durante todo el proyecto 
def menu(opciones):
    for i, opcion in enumerate(opciones):
        print(f"{i+1}. {opcion}")
    
    opcion = input("ingrese el numero de la opcion que desea elegir: ")
    while not opcion.isnumeric() or not int(opcion) in range(1, len(opciones)+1):
        opcion = input("Error, ingrese el numero de la opcion que desea elegir: ")

    opcion = int(opcion)-1

    return opcion


#funciones de usuario comun 

def login(usuarios,posts, persona_activa,likes,comentarios):
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
        

    for user in usuarios:
        if user.username.lower() == username.lower():
            return user
    
    return 1

#funciones de inicio de sesión
def menu_log_sign(usuarios,posts,likes,comentarios):
    opciones_usuario_comun = ["Log in", "Sign up", "Cerrar programa"]
    opcion_usuario_comun = menu(opciones_usuario_comun)

    
    if opcion_usuario_comun ==0:
        persona_activa = login(usuarios,posts,1,likes,comentarios) #verificación de que el usuario este en la lista de usuarios
        if persona_activa == 1:
            print("No existe este usuario en la base de datos ")
            menu_log_sign(usuarios,posts,likes,comentarios)
        else: #en caso de que esté te manda al inicio (home)
            home(usuarios,posts, persona_activa,likes,comentarios)
    elif opcion_usuario_comun == 1:
        persona_activa  = signup(usuarios)

        home(usuarios,posts, persona_activa,likes,comentarios)
    else:
        pass
    
#funciones de registro en caso de no tener cuenta activa
def signup(usuarios):
    nombre = input("Ingrese su nombre: ") #String - letras
    while not nombre.isalpha():
        nombre = input("Error, Ingresa el nombre: ")

    apellido = input("Ingrese su apellido: ") #String - letras
    while not apellido.isalpha():
        apellido = input("Error, Ingresa su apellido: ")

    correo = input("Ingrese su correo electrónico (unimet): ") #String tiene: @unimet.edu.ve
    while not "@unimet.edu.ve" in correo:
        correo = input("Error, ingrese un correo válido")

    username = input("Ingrese un nombre de usuario: @") #String no tiene: @
    username = username.replace("@", "")


    tipo = input("Estudiante (1) o profesor (2): ") #String una P o E, 
    while not tipo.isnumeric() or not int(tipo) in range(1, 3):
        tipo = input("Error, ingrese la inicial correspondiente a su elección: ")
    
    id = username

    following = []

    
    if tipo == "E":
        tipo = "Estudiante"
        carrera = input("Ingrese la carrera que está cursando")
        for user in usuarios:
            if user.tipo == 'estudiante':
                if user.carrera == carrera.lower():
                    following.append(user.id)

        nuevo_user = Estudiante(id,nombre,apellido,correo,username, following,tipo, carrera)
        
    elif tipo == "P":
        tipo = "Profesor"
        departamento = input("Ingrese el departamento al que pertence: ")
        for user in usuarios:
            if user.tipo == 'profesor':
                if user.departamento == departamento.lower():
                    following.append(user.id)
        nuevo_user = Profesor(id,nombre,apellido,correo,username, following,tipo, departamento)

    usuarios.append(nuevo_user)
    return nuevo_user

# home/ inicio / menu de opciones principal 
def home(usuarios,posts, persona_activa,likes,comentarios):
    while True:
        print("")
        #dependiendo de la opción elegida llamamos a la funcion 
        opciones_home = ["Inicio", "Búsqueda", "Crear publicación", "Perfil", "Salir"] #menu de opciones principal
        opcion_home = menu(opciones_home)
        if opcion_home == 0:
            home_inicio(posts, usuarios, persona_activa,likes,comentarios)
        elif opcion_home == 1:
            home_busqueda(usuarios,posts,likes,comentarios,persona_activa)
        elif opcion_home == 2:
            home_publicar(posts,persona_activa)
        elif opcion_home == 3:
            home_perfil(usuarios,persona_activa,posts,likes,comentarios)
        else:
            menu_log_sign(usuarios,posts,likes,comentarios)
            break
          

def home_inicio(posts, usuarios, persona_activa,likes,comentarios):
    #obtengo el pefil del usuario activo y guardo los seguidos en la variable vacia
    seguidos = persona_activa.following
            
    #si esta en la lista de seguidos le aplico el metodo y lo muestro
    posts_nuevos = []
    counter = 1
    for post in posts:
        if post.username in seguidos:
            print(counter)
            post.show_inicio()
            posts_nuevos.append(post)
            counter+=1
    
    opcion_post_interaccion = input("Ingrese el número de post con el que desea interactuar, si no dese interactuar con niguno coloque (0): ")
    while not opcion_post_interaccion.isnumeric() or not int(opcion_post_interaccion) in range(0,len(posts_nuevos)+1):
        opcion_post_interaccion = input("Error, ingrese el numero de la opcion que desea elegir: ")
    
    interactuar_con_post(opcion_post_interaccion,usuarios,likes,posts_nuevos,posts,comentarios,post,persona_activa)

#perfil_interactuar es el usuario con el que vamos a interactuar
def interactuar_con_perfil(perfil_interactuar,usuarios,usuarios_mostrados, persona_activa,posts,likes,comentarios):
    perfil_interactuar = usuarios_mostrados[int(perfil_interactuar)]

    opciones_perfil_interaccion = ["Seguir","Dejar de seguir","Entrar al perfil","Salir"]
    opcion_perfil_interaccion = menu(opciones_perfil_interaccion)

    #Si quieres seguir al usuario, primero nos aseguramos de que el id del usuario con el que estamos interactuando
    #no este en tus followings, si está se imprime el mensaje, sino appendeamos el perfil a tu lista de following (la del perfil que esta usando el programa)
    if opcion_perfil_interaccion ==0:
        if perfil_interactuar.id in persona_activa.following:
            print("Ya sigues a esta persona")
        else:
            persona_activa.following.append(perfil_interactuar.id)
            print("Seguido")

    if opcion_perfil_interaccion ==1:
        if perfil_interactuar.id in persona_activa.following:
            persona_activa.following.remove(perfil_interactuar)
            print("Dejaste de seguir")
        else:
            print("No sigues a esta cuenta")
        #perfil_interactuar es un objeto por lo que aplicamos el metodo perfil, que nos lleva a su perfil, entonces
        #  el perfil puede devolverte una lista con la posicion que deseas interacturar y las variables (post) para poder hacerlo
    if opcion_perfil_interaccion ==2:
        info = perfil_interactuar.perfil(posts, persona_activa)
        opcion_post_interaccion = info[0]
        posts_user = info[1]
        interactuar_con_post(opcion_post_interaccion,usuarios,likes,posts_user,posts,comentarios,posts_user[int(opcion_post_interaccion)-1],persona_activa)
    
    if opcion_perfil_interaccion ==3:
        home(usuarios,posts, persona_activa,likes,comentarios)

#funciones para ver likes y comentarios y borrarlos
def interactuar_con_post_propio(opcion_post_interaccion,usuarios,likes,posts_nuevos,posts,comentarios,post,persona_activa):
    if int(opcion_post_interaccion)!=0:
        opciones_interaccion_mi_post = ["Ver likes", "Ver comentarios", "Eliminar likes", "Eliminar comentarios"]
        opcion_interaccion_mi_post = menu(opciones_interaccion_mi_post)
        #recorremos la lista de likes, si el username del post donde se encuentra el like
        #  coincide con el id de la persona activda se le suma 1 al contador y agregamos ese username a la lista de likes
        if opcion_interaccion_mi_post == 0:
            contador = 0
            likes_perfiles = []
            print("Lista de Likes")
            for like in likes:
                if like.post.username == persona_activa.id:
                    contador += 1
                    print(contador)
                    like.show()
                    likes_perfiles.append(like.post.username)
        
            
            print(f"En total tienes {contador} likes")
            #a partir de la lista mostrada se puede entrar al perfil del usuario
            opcion_like_interaccion = input("Si desea entrar a un perfil, ingresa el número de like correspodiente al perfil que desea entrar, de lo contrario presione (0)")
            while not opcion_like_interaccion.isnumeric() or not int(opcion_like_interaccion) in range(0,contador+1):
                    opcion_like_interaccion = input("Error, ingrese el numero de la opcion que desea elegir: ")
            

            if int(opcion_like_interaccion) != 0:
                var = ""
                for user in usuarios:
                    # si el id del user es igual al numero de elección:
                    if user.id == likes_perfiles[int(opcion_like_interaccion)-1]:
                        var = user
                    

                interactuar_con_perfil(opcion_like_interaccion,usuarios,likes_perfiles, persona_activa,posts,likes,comentarios)










        elif opcion_interaccion_mi_post == 1:
            contador = 0
            print("Lista de Comentarios")
            for comentario in comentarios:
                if comentario.post.username == persona_activa.id:
                    contador += 1
                    print(contador)
                    comentario.show()
        
        elif opcion_interaccion_mi_post == 2:
            contador = 0
            print("Lista de Likes")
            for like in likes:
                if like.post.username == persona_activa.id:
                    contador += 1
                    print(contador)
                    like.show()
            #El usuario selecciona el número de like que quiere borrar 
            opcion_like_interaccion = input("Ingrese el número de Like que desea eliminar, si no desea eliminar ninguno pulse (0): ")
            while not opcion_post_interaccion.isnumeric() or not int(opcion_like_interaccion) in range(0,contador+1):
                opcion_like_interaccion = input("Error, ingrese el numero de la opcion que desea elegir: ")
            #Si el numero correspondiente al like, corresponde con el numero seleccionado se elimina
            contador = 0
            for like in likes:
                if like.post.username == persona_activa.id:
                    contador += 1
                    if contador == int(opcion_like_interaccion):
                        likes.remove(like)
            

        
        elif opcion_interaccion_mi_post == 3:
            contador = 0

            print("Lista de Comentarios")
            for comentario in comentarios:
                if comentario.post.username == persona_activa.id:
                    contador += 1
                    print(contador)
                    comentario.show()
            #el usuario selecciona el número de comentario que desea eliminar 
            opcion_comentario_interaccion = input("Ingrese el número de comentario que desea eliminar, si no desea eliminar ninguno, pulse (0): ")
            while not opcion_comentario_interaccion.isnumeric() or not int(opcion_comentario_interaccion) in range(0,contador+1):
                opcion_comentario_interaccion = input("Error, ingrese el numero de la opcion que desea elegir: ")

            contador = 0
            for comentario in comentarios:
                if comentario.post.username == persona_activa.id:
                    contador += 1
                    if contador == int(opcion_comentario_interaccion):
                        comentarios.remove(comentario)
        




def interactuar_con_post(opcion_post_interaccion,usuarios,likes,posts_nuevos,posts,comentarios,post,persona_activa):
    if int(opcion_post_interaccion) != 0:
        opciones_interacciones = ["Likear", "Comentar", "Ingresar al perfil", "Salir"]
        opcion_interacciones = menu(opciones_interacciones)

        id_usuario = posts_nuevos[int(opcion_post_interaccion)-1].username
        #convertimos la clase like en un objeto para luego appendearlo a la lista 
        if opcion_interacciones == 0:
            for user in usuarios:
                if user.id == id_usuario:
                    like = Like(post,persona_activa)
                    likes.append(like)
                    print ("❤️")
                    
                    break

        elif opcion_interacciones == 1:
            comentario = input("Ingrese su comentario: ")
            for user in usuarios:
                if user.id == id_usuario:
                    nuevo_comentario = Comentario(persona_activa,posts_nuevos[int(opcion_post_interaccion)-1],comentario,"hoy")
                    comentarios.append(nuevo_comentario)
                    print("💬")
        
        elif opcion_interacciones == 2:
            
            for user in usuarios:
                if id_usuario == user.id:
                    opcion_post_interaccion = user.perfil(posts, persona_activa)
                    print(opcion_post_interaccion)
                    if opcion_post_interaccion != '0':
                        posts_nuevos = []
                        for post in posts:
                            if post.username == id_usuario:
                                posts_nuevos.append(post)

                        opciones_interacciones = ["Likear", "Comentar", "Salir"]
                        opcion_interacciones = menu(opciones_interacciones)

                        if opcion_interacciones == 0:
                            for user in usuarios:
                                if user.id == id_usuario:
                                    like = Like(posts_nuevos[int(opcion_post_interaccion)-1],persona_activa)
                                    likes.append(like)
                                    print ("❤️")
                                    
                                    break

                        elif opcion_interacciones == 1:
                            comentario = input("Ingrese su comentario: ")
                            for user in usuarios:
                                if user.id == id_usuario:
                                    nuevo_comentario = Comentario(persona_activa,posts_nuevos[int(opcion_post_interaccion)-1],comentario,"hoy")
                                    comentarios.append(nuevo_comentario)
                                    print("💬")
                        
                            
                    
        
        
        elif opcion_interacciones == 3:
            home(usuarios,posts, persona_activa,likes,comentarios)
                            
                            

            







 
    #opciones_interacciones1 = [" publica"]

#funciones de búsqueda
def home_busqueda(usuarios,posts,likes,comentarios,persona_activa):
    print("Que desea buscar? ")
    opciones_busqueda=["Usuario","Publicación"]
    opcion_busqueda = menu(opciones_busqueda)
    
    #Búsqueda de usuario
    if opcion_busqueda ==0:
        print("Busqueda de usuarios a través de: ")
        opciones_busqueda_usuario = ["Username", "Carrera o departamento"]
        opcion_busqueda_usuario = menu(opciones_busqueda_usuario)
        
        if opcion_busqueda_usuario==0:
            counter = 0
            busqueda_username = input("Ingrese el username que esta buscando ")
            user0 = ""
            for user in usuarios:
                if busqueda_username.lower() == user.username.lower():
                    user.show()
                    user0 = user
                    counter+=1

            if counter == 0:
                print("No se han encontrado resultados a tu búsqueda")
                #si el usuario se encuentra en la lista de usuarios, se muestra el perfil y agregarmos 1 al counter, si el counter da 0 significa que no está 
            else:
                interactuar_con_perfil(0,usuarios,[user0], persona_activa,posts,likes,comentarios)
                
        #Búsqueda de usuario por de departamento/ carrera
        elif opcion_busqueda_usuario== 1:
            busqueda_cd = input("Ingrese la carrera o departamento del usuario que desea buscar: ")
            perfiles = []
            counter = 1
            for user in usuarios:
                if user.tipo == "profesor":
                    if busqueda_cd.lower() == user.departamento.lower():
                        print(counter)
                        user.show()
                        perfiles.append(user)
                        counter+=1
                    

                    
                elif user.tipo == "estudiante":
                    if busqueda_cd.lower() == user.carrera.lower():
                        print(counter)
                        user.show()
                        perfiles.append(user)
                        counter=+1
        
            
            opcion_perfil_interaccion = input("Ingrese el número de perfil con el que desea interactuar, si no dese interactuar con niguno coloque (0): ")
            while not opcion_perfil_interaccion.isnumeric() or not int(opcion_perfil_interaccion) in range(0,len(perfiles)+1):
                    opcion_perfil_interaccion = input("Error, ingrese el numero de la opcion que desea elegir: ")
            


            if int(opcion_perfil_interaccion) != 0:
                interactuar_con_perfil(int(opcion_perfil_interaccion)-1,usuarios,perfiles, persona_activa,posts,likes,comentarios)
                        
                      
            if counter == 0:
                    print("No se han encontrado resultados a tu búsqueda")
            #mismo proceso que con el usuario


    elif opcion_busqueda ==1:
        print("Busqueda de post a través de: ")
        opciones_busqueda_publicacion = ["Username", "Hashtag"]
        opcion_busqueda_publicacion = menu(opciones_busqueda_publicacion)
        if opcion_busqueda_publicacion == 0:
            counter = 0
            id = ""
            post = ""
            
            busqueda_username = input("Ingrese el username que esta buscando ")
            for user in usuarios:
                if busqueda_username.lower() == user.username.lower():
                    id = user.id
                    counter+=1

            if counter != 0:
                while True:
                    if id in persona_activa.following:
                        posts_de_perfil = []
                        counter = 1
                        for post in posts:
                            if id == post.username:
                                print(counter)
                                post.show()
                                posts_de_perfil.append(post)
                                counter+=1
                    
                        opcion_post_interaccion = input("Ingrese el número de post con el que desea interactuar, si no dese interactuar con niguno coloque (0):")
                        while not opcion_post_interaccion.isnumeric() or not int(opcion_post_interaccion) in range(0,len(posts_de_perfil)+1):
                            opcion_post_interaccion = input("Error, ingrese el numero de la opcion que desea elegir: ")
                        
                        if int(opcion_post_interaccion) != 0:
                            interactuar_con_post(opcion_post_interaccion,usuarios,likes,posts_de_perfil,posts,comentarios,post, persona_activa)
                        else:
                            break
                    else:
                        print("No sigue a este usuario, desea seguirlo?")

                        opciones_seguir = ["Si", "No"]
                        for i, opcion in enumerate(opciones_seguir):
                            print(f"{i+1}. {opcion}")
                        
                        opcion = input("ingrese el numero de la opcion que desea elegir: ")
                        while not opcion.isnumeric() or not int(opcion) in range(1, len(opciones_seguir)+1):
                            opcion = input("Error, ingrese el numero de la opcion que desea elegir: ")

                        opcion = int(opcion)-1
                        if opcion == 0:
                            persona_activa.following.append(id)
                        else:
                            break

            elif counter == 0:
                print("No se han encontrado resultados a tu búsqueda")
            


        

        if opcion_busqueda_publicacion == 1:
            busqueda_hashtag = input("Ingrese el hashtag: ")
            counter = 1
            counter2 = 0
            posts_de_perfil = []
            for post in posts:
                if busqueda_hashtag in post.hashtag and post.username in persona_activa.following:
                    print(counter)
                    counter=counter+1
                    counter2=counter2+1
                    posts_de_perfil.append(post)
                    post.show()
                    
                    
            
            
            if counter2 == 0:
                print("No se han encontrado resultados a tu búsqueda")
            else:
                opcion_post_interaccion = input("Ingrese el número de post con el que desea interactuar, si no dese interactuar con niguno coloque (0): ")
                while not opcion_post_interaccion.isnumeric() or not int(opcion_post_interaccion) in range(0,len(posts_de_perfil)+1):
                    opcion_post_interaccion = input("Error, ingrese el numero de la opcion que desea elegir: ")
                
                interactuar_con_post(opcion_post_interaccion,usuarios,likes,posts_de_perfil,posts,comentarios,post,persona_activa)

#funciones de publicar un post    
def home_publicar(posts, persona_activa):
    tipo = input("Ingrese el tipo de multimedia que va a publicar: Foto(F) o Video(V): ")
    while tipo.lower() != "f" and tipo.lower() != "v":
        tipo = input("Error, ingrese la inicial correspondiente a su elección") #verificacion - que sea V o F
    
    if tipo == "F":
        tipo = "Foto"
    else:
        tipo = "Video"
    
    url = input("Ingrese el url de su publicación: ")

    caption = input("Ingrese el caption: ")
    while len(caption)>2200:                        #validación de que no sobrepase el limite de palabras
        caption = input("Ha exedido el límite de 2200 caracteres. Ingrese nuevamente el caption: ") 

    hashtag = input("Ingrese un hashtag: #")
    hashtag = hashtag.replace("#", "")

    date_post = date.today()

    #convertimos la clase Post con sus atributos en un objeto, el cual agrergamos a la lista de posts
    publicacion= Post(persona_activa,tipo,url, caption,hashtag,date_post)
    posts.append(publicacion)
    print("⬆ Post Publicado! ⬆")


#funciones para modificar o eliminar perfil, aqui se incluye también la interacción del usuaio con sus propios posts   
def home_perfil(usuarios,persona_activa,posts,likes,comentarios):

    opciones_home_perfil = ["Modificar información", "Eliminar cuenta", "Ver mis posts"]
    opcion_home_perfil = menu(opciones_home_perfil)
    if opcion_home_perfil ==0:
        print("Que área de su información desea modificar?")
        opciones_modifdicacion = ["Nombre", "Apellido", "Correo", "Username", "Tipo"]
        opcion_modificacion = menu(opciones_modifdicacion)

        if opcion_modificacion ==0:
            nombre = input("Ingrese su nombre: ") #verifiación - String - letras
            while not nombre.isalpha():
                nombre = input("Error, Ingresa el nombre: ")


            for user in usuarios:
                if persona_activa.id == user.id:
                    user.nombre = nombre
                    persona_activa.nombre = nombre
                    print("Cambio exitoso!")

        elif opcion_modificacion ==1:
            apellido = input("Ingrese su apellido: ") #verificacion - String - letras
            while not apellido.isalpha():
                apellido = input("Error, Ingresa su apellido: ")
            for user in usuarios:
                if persona_activa.id == user.id:
                    user.apellido = apellido
                    persona_activa.apellido = apellido 
                    print("cambio exitoso")
            
        elif opcion_modificacion ==2:
            while True:
                correo = input("Ingrese su correo electrónico (unimet): ") #verificación - String tiene: @unimet.edu.ve
                while not "@unimet.edu.ve" in correo:
                    correo = input("Error, ingrese un correo válido")
                
                contador = 0
                for user in usuarios:
                    if correo == user.correo:
                        contador = contador + 1
                if contador == 0:
                    for user in usuarios:
                        if persona_activa.id == user.id:
                            user.correo = correo
                            persona_activa.correo = correo
                            print("cambio exitoso")
                    break
                #utilizamos contador para verificar que no exista ya la dirección de correo en la base de datos, si luego de recorrer la lista, no se le suma 1, no existe 
                else:
                        print("Este correo electrónico ya está vinculado a una cuenta, intente nuevamente")
         
        elif opcion_modificacion ==3:
            while True:
                username = input("Ingrese un nombre de usuario: @") #verificación - String no tiene: @
                username = username.replace("@", "")
                
                contador = 0
                for user in usuarios:
                    if username == user.username:
                        contador = contador + 1
                #verificación de que no haya un perfil en la base de datos con el mismo nombre de usuario 
                if contador == 0:
                    for user in usuarios:
                        if persona_activa.id == user.id:
                            user.username = username
                            persona_activa.username = username
                            print("cambio exitoso")
                    break
                else:
                    print("Ya existe un perfil con este nombre de usuario, intente nuevamente")
            
        elif opcion_modificacion ==4:

            tipo = input("Estudiante (E) o profesor (P): ") #verificación - String una P o E, 
            while tipo.upper() != "P" and tipo.upper() != "E":
                tipo = input("Error, ingrese la inicial correspondiente a su elección")
                
            for user in usuarios:
                if persona_activa.id == user.id:
                    if tipo.upper() == "E":
                        carrera = input("Ingrese la carrera que está cursando: ") 
                        cambio_usuario= Estudiante(user.id,user.nombre, user.apellido ,user.correo,user.username, user.following, "estudiante",carrera)
                        usuarios.remove(user)
                        usuarios.append(cambio_usuario)
                        #se utiliza la clase Estudiante para convertirla en el objeto cambio_usuario y 
                        # este objeto agregarlo a la lista de usuarios

                    elif tipo.upper() == "P":
                        departamento = input("Ingrese el departamento al que pertence: ")
                        cambio_usuario= Profesor(user.id,user.nombre, user.apellido ,user.correo,user.username, user.following, "profesor",departamento)
                        usuarios.remove(user)
                        usuarios.append(cambio_usuario)
                        #se utiliza la clase Profesor para convertirla en el objeto cambio_usuario 
                        # y este objeto agregarlo a la lista de usuarios

                



    if opcion_home_perfil == 1: 
        print("Está seguro de que desea eliminar su cuenta? Se borrara toda la información guardada")
        opciones = ["Si, deseo eliminar mi cuenta", "No"]
        opcion = menu(opciones) 
        #se elimina el usuario de la lista de usuarios
        if opcion ==0:
            for indice, user in enumerate(usuarios):
                print(persona_activa.id, user.id)
                if persona_activa.id == user.id:
                    del usuarios[indice]
                    break
            #se elimina a parte toda su información de cada lista (posts,likes,comentarios)
            for post in posts:
                if persona_activa.id == post.username:
                    posts.remove(post)
            for like in likes:
                if persona_activa.id == like.username:
                    likes.remove(like)
            for comentario in comentarios:
                if persona_activa.id == comentario.username:
                    comentarios.remove(comentario)
                    

            print("Ha eliminado su cuenta con éxito!")
            menu_log_sign(usuarios,posts,likes,comentarios)

        if opcion==1:
            home_perfil()

    if opcion_home_perfil ==2:
        posts_perfil = []
        counter = 1
        for post in posts:
            if post.username == persona_activa.id:
                print(counter)
                post.show()
                posts_perfil.append(post)
                counter+=1
    
        opcion_post_interaccion = input("Ingrese el número de post con el que desea interactuar, si no dese interactuar con niguno coloque (0): ")
        while not opcion_post_interaccion.isnumeric() or not int(opcion_post_interaccion) in range(0,len(posts_perfil)+1):
            opcion_post_interaccion = input("Error, ingrese el numero de la opcion que desea elegir: ")
        
        interactuar_con_post_propio(opcion_post_interaccion,usuarios,likes,posts_perfil,posts,comentarios,post,persona_activa)

#funciones de usuario adminitrador 

def moderador(usuarios,posts,comentarios,usuarios_eliminados,likes ):
    #menu de opciones del moderador 
    opciones_moderador = ["Eliminar post ofensivo","Eliminar comentario ofensivo","Eliminar usuario por infracción de reglas"]
    opcion_moderador = menu(opciones_moderador)
    if opcion_moderador == 0:    
        contador = 0
        #recorremos la lista de post y los imprimimos con su contador
        for post in posts:
            contador+=1
            print(contador)
            post.show()

        opcion_post_eliminar = input("Ingrese el número de post correspondiente al que desea eliminar: ")
        while not opcion_post_eliminar.isnumeric() or not int(opcion_post_eliminar) in range(0,contador+1):
            opcion_post_eliminar = input("Error, ingrese el numero de la opcion que desea elegir: ")
   #si post seleccionado corresponde al numero de post este se borra
        post_seleccionado = posts[len(opcion_post_eliminar)-1]
        posts.remove(post_seleccionado)
    #borramos de igual manera sus comentarios y sus likes 
        for comentario in comentarios:
            if comentario.post == post_seleccionado:
                comentarios.remove(comentario)

        for like in likes:
            if like.post ==post_seleccionado:
                likes.remove(like)



    elif opcion_moderador == 1:
        contador=0
        for comentario in comentarios:
            contador+=1
            print(contador)
            comentario.show()
    
        if len(comentarios) != 0:
            opcion_post_interaccion = input("Ingrese el número del comentario que desea borrar: ")
            while not opcion_post_interaccion.isnumeric() or not int(opcion_post_interaccion) in range(0,contador+1):
                opcion_post_interaccion = input("Error, Ingrese el número del comentario que desea borrar: ")

                comentarios.remove(comentarios[len(opcion_post_interaccion)-1])
        else:
            print("no hay comentarios")
#recorremos lista de usuarios e imprimimos con su contador 
    elif opcion_moderador ==2:
        contador = 0
        for usuario in usuarios:
            contador+=1
            print(contador)
            usuario.show()

        opcion_usuario_eliminar = input("Ingrese el número de usuario al cual desea eliminar: ")
        while not opcion_usuario_eliminar.isnumeric() or not int(opcion_usuario_eliminar) in range(0,contador+1):
            opcion_usuario_eliminar = input("Error, ingrese el numero de la opcion que desea elegir: ")

        usuarios.remove(usuarios[len(opcion_usuario_eliminar)-1])
        #agregamos tambien el usuario seleccionado a la lista de usuarios eliminados para cuando se hacen las estadisticas
        usuarios_eliminados.append(usuarios[len(opcion_usuario_eliminar)-1])




def estadisticas(posts, usuarios,likes,comentarios,usuarios_eliminados):
    #menu de opciones de mostrar estadísticas, a partir de esta elección se generan los respectivos informes 
   
    opciones_estadisticas = ["Generar informes de publicaciones", "Generar informes de interacción","Generar informes de moderación "]
    opcion_estadisticas = menu(opciones_estadisticas)


    if opcion_estadisticas == 0:
        counter = 0
        usuario_con_mas = ""
        for post in posts:
            counter = max(counter,post.usuarios)
            if counter == post.usuarios:
                usuario_con_mas = post.username

        print(f"""Informe de publicaciones:
                - Top 3 de usuarios con mayor cantidad de publicaciones: {usuario_con_mas}
                - Top 3 de carreras con mayor cantidad de publicaciones:
              
              
              
              
              Se ha generado un informe en base a los siguientes datos:
- Usuarios con mayor cantidad de publicaciones: 
- Carreras con mayor cantidad de publicaciones: """)


    elif opcion_estadisticas == 1:
        print(f"""Informe de interacciones:
- Post con la mayor cantidad de interacciones: 
- Usuarios con la mayor cantidad de interacciones (dadas y enviadas):
""")

    
    elif opcion_estadisticas == 2:
        print(f"""Informe de moderación:
- Usuarios con la mayor cantidad de post tumbados
- Carreras con mayor comentarios inadecuados. 
- Usuarios eliminados por infracciones: {usuarios_eliminados}
""")


    







###########################################################################################

#funciones de usuario admin 


