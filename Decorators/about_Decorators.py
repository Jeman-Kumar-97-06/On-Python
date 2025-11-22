#First Class Functions : 
#   Treated as first-class citizens.
#   They are just handled how strings, ints are handled.
#   They can be assigned to values : 
def greet(name):
    return f'hello, {name}'

my_greet_func = greet
print(my_greet_func('jeman'))

#   They can be passed as args to other functions:
def apply_op(func,value):
    return func(value)

def square(x):
    return x*x

print(apply_op(square,8))

#   They can be return values of other functions.
#   They can also be elements of lists, dicts or sets.

#Closure:
def outer_f(msg):
    message = msg
    def inner_function():
        print(message)
    return inner_function

my_func = outer_f('HI') # outer_f is done with execution. The memory is cleared. But the inner function still remembers 'message'
my_func()

#Decorators
# A Decorator is a function fx that takes fy as arg and adds some
# xtra functionality and returns a new fz without altering the 
# original fy that we sent as the arg.

#Example1 :
def decorator_1(og_f):
    print(og_f) #-------------------------------> LocationX
    def wrapper_fun():
        return og_f()
        # return og_f
    return wrapper_fun

def display():
    print("Display function ran!")

decorated_display = decorator_1(display)
print(decorated_display()) #--------------------> LocationX
decorated_display()

#Example2 : Same as the above. But with Decorator syntax:
def decorator_2(og_f):
    def wrapper_f():
        print("Wrapper function ran!")
        return og_f()
    return wrapper_f

@decorator_2
def display():
    print("Display function ran yo!")

display()

#Example3 : Using decorators on functions with args:
def decorator_3(og_f):
    def wrapper_f(*args,**kwargs):
        print("Ran Wrapper")
        return og_f(*args,**kwargs)
    return wrapper_f

@decorator_3
def display(name,age):
    print('display ran with arguments {} & {}'.format(name,age))

display("John",28)

#Example4 : The WRAPS decorator : 
#without WRAPS:
def log(func):
    def wrapper(*args, **kwargs):
        print(f'calling {func.__name__}')
        return func(*args,**kwargs)
    return wrapper

@log
def greet(name):
    """Greets a person by name"""
    print(f"Hello {name}")

print(greet.__name__) #This prints 'wrapper'
print(greet.__doc__)  #This prints 'None'

#with WRAPS:
from functools import wraps
def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"calling {func.__name__}")
        return func(*args,**kwargs)
    return wrapper

@log
def greet(name):
    """"Greets a person by name"""
    print(f'Hello {name}')

print(greet.__name__) #This prints 'greet'
print(greet.__doc__)  #This prints "Greets a person by name"