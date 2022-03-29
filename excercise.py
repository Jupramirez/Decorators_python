

#decorador
from ast import arg


def logging_decorator(function):
    def wrapper(*args,**kwargs):
        name_function = function.__name__
        num = function(args)
        print(f"you called {name_function} {args} \n It returned:{num}")
    return wrapper


@logging_decorator
def a_function(*args):                                         
    sum = 0
    for num in args[0]:
        sum += num
    return sum

a_function(1,2,3,4,5,7) 