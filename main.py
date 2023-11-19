#Importaciones de las clases 
from Username import *
from Post import *
from Like import *
from Comentario import *
from Profesor import *
from Estudiante import *

#Importacion del archivo donde estan las funciones 
import funciones
import json



def main():
    
    usuarios = []
    posts = []
    comentarios = []
    likes = []
    usuarios_eliminados = []


    funciones.extraccion_info(usuarios,posts,likes,comentarios )


    while True:
        print("Bienvenido a Metrogram")
        #****Inicio*** En donde se pregunta que tipo de usuario eres
        opciones_inicio = ["Usuario Común", "Usuario Administrador", "Salir"]
        opcion_inicio = funciones.menu(opciones_inicio)

        if opcion_inicio == 0:
            funciones.menu_log_sign(usuarios,posts,likes,comentarios)

        elif opcion_inicio == 1:

            #Este es el submenu del area administrativa
            opciones_administrador = ["Moderador", "Estadísticas"]
            opcion_administrador = funciones.menu(opciones_administrador)
            if opcion_administrador ==0:

                funciones.moderador(usuarios,posts,comentarios, usuarios_eliminados)

            elif opciones_administrador ==1:

                funciones.estadisticas(posts, usuarios,likes,comentarios,usuarios_eliminados)
        else:
            funciones.guardado_info(usuarios,posts,likes,comentarios )
            
            break
            










main()

