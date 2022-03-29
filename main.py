
#creacion de la clase usuario
class User:
    def __init__(self,name):
        self.name = name
        self.is_logged_in = False
#decorador 
#acepta argumentos args(tuplas) y kwargs (dic), si esta logg hace la funcion
def is_authenticated_decorator(function):
    def wrapper(*args,**kwargs):
        if args[0].is_logged_in:
            function(args[0])
    return wrapper
#se le pasa el decorador a la funcion de crear blog
@is_authenticated_decorator
def create_blog_post(user):
    print(f"this is {user.name}'s new blog post.")

new_user = User("Juan")
new_user.is_logged_in = True
create_blog_post(new_user)