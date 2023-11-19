class Comentario():
    def __init__(self,username,post,comentario,date):
        self.username = username
        self.post = post
        self.comentario = comentario 
        self.date = date


    def show(self):
        post = self.post
        print(f"""
            post: 
                {post.tipo}
                {post.url}
            username: {self.username.username}
            comentario: {self.comentario}
            Fecha de publicación : {self.date}
        """)    




