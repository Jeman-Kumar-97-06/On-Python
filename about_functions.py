import math
print("Every fucking thing in math module:")
print(dir(math))

import random
print("Every fucking thing in random module:")
print(dir(random))

def func_name(param1, param2):
    result = param1 + param2
    return result

def func_no_params():
    print("function with no parameters is executed!")

def func_default_params(name='Jeman'):
    print(f'Hello, {name}')

def variables_args_kwargs(*args, **kwargs):
    print(args)
    print(len(args))
    print(args[1])
    print(kwargs)
    print(kwargs.keys())
    print(kwargs.values())