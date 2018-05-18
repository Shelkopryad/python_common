
def call(method, *args, **kwargs):
    return method(*args, **kwargs)

def print_args(*args, **kwargs):
    for x in zip(*args, **kwargs):
        print(x)
    
def do_something():
    print("Hello")


call(print_args, [1,2,3,4], [5,6,7,8])