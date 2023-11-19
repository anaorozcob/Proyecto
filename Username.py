
class Username():
    def __init__(self,id,nombre,apellido,correo,username, following,tipo):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.username = username
        self.tipo = tipo
        self.following = following

    def show(self):
        print(f"""
            Id :{self.id}
            Nombre: {self.nombre}
            Apellido : {self.apellido}
            Correo : {self.correo}
            Username: {self.username}
            Tipo: {self.tipo}  
            following: {len(self.following)}
        """)

    #EL perfil de un usuario cualquiera, aqui vemos nombre, username y post de un usuario
    def perfil(self,posts, persona_activa):

        print(f"""
        {self.nombre}
        {self.username}
        """)

        while True:
            if self.id in persona_activa.following:
                posts_user= []
                counter = 1
                for post in posts:
                    if post.username == self.id:
                        print(counter)
                        post.show_inicio()
                        posts_user.append(post)
                        counter+=1
                            
                    
                opcion_post_interaccion = input("Ingrese el número de post con el que desea interactuar, si no dese interactuar con niguno coloque (0): ")
                while not opcion_post_interaccion.isnumeric() or not int(opcion_post_interaccion) in range(0,len(posts_user)+1):
                        opcion_post_interaccion = input("Error, ingrese el numero de la opcion que desea elegir: ")
                
                
                return [opcion_post_interaccion, posts_user]

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
                    persona_activa.following.append(self.id)
                else:
                    return 0
                

                
