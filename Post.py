class Post():
    def __init__(self,username,tipo,url, caption,hashtag,date):
        self.username = username
        self.tipo = tipo
        self.url = url
        self.caption = caption
        self.hashtag = hashtag
        self.date = date


    def show(self):
        print(f"""
            Username: {self.username}
            Caption : {self.caption}
            Date : {self.date}
            Tags: {self.hashtag}
            tipo: {self.tipo} 
            Url: {self.url}    
        """)

    def show_inicio(self):
        print(f"""
            @{self.username}
            -----------
            {self.tipo} 
            -----------
            {self.caption}
            {self.hashtag}


            {self.date}  
            ------------------------------------------------------------------------------------
            
        """)

