from Username import *

class Estudiante(Username):
    def __init__(self,id,nombre,apellido,correo,username, following,tipo,carrera):
        super().__init__(id, nombre, apellido,correo,username, following,"estudiante")
        self.carrera = carrera
        

    def show(self):
        print(f"""
            Id :{self.id}
            Nombre: {self.nombre}
            Apellido : {self.apellido}
            Correo : {self.correo}
            Username: {self.username}
            Tipo: {self.tipo}  
            Carrera: {self.carrera}
            following: {len(self.following)}
        """)
