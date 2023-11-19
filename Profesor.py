from Username import *

class Profesor(Username):
    def __init__(self,id,nombre,apellido,correo,username, following,tipo,departamento):
        super().__init__(id, nombre, apellido,correo,username, following,"profesor")
        self.departamento = departamento
        

    def show(self):
        print(f"""
            Id :{self.id}
            Nombre: {self.nombre}
            Apellido : {self.apellido}
            Correo : {self.correo}
            Username: {self.username}
            Tipo: {self.tipo}  
            Departamento: {self.departamento}
            following: {len(self.following)}
        """)
