class Like():
    def __init__(self,post,username):
        self.post = post
        self.username = username 
        

    def show(self):
        post = self.post
        print(f"""
            post: 
                {post.tipo}
                {post.url}
            username: {self.username.username}
        """)

    