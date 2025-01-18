import math
import random
import matplotlib.pyplot as py
print(f'Isha Gill has {len('Isha Gill')} letters')
print(f'square_root of 2 is {math.sqrt(2):.3f}')
print(random.randint(1,10))
print(random.randint(1,10))
print(random.randint(1,10))
print(random.randint(1,10))
print(random.randint(1,10))
def some_function():
    "Happy thursday"

def double_this(something_to_double:int) :
    print(something_to_double*2)
some_function()
double_this(10)
def multiply_this(first:float,second:float):
    print(first*second)

multiply_this(2,3)
# default values
def print_citation(author:str,publisher:str="",year:int=""):
    print(f'Some citation {author},{publisher},({year})')

print_citation("Isha")
#named arguments doesn't require positional order
print_citation("Isha",year=2025)
def print_face(character:str):
    print(f' {character} {character}')
    print(f'  {character}')

    print(character*5)
print_face('*')
def print_body():
    print('|      |')
    print('/      \ ')
    print('|      |')
    print('|      |')
# function as an argument
def print_character(letter:str,head_function,body_function):
    head_function(letter)
    body_function()
    # no parenthesis for function
print_character('*',print_face,print_body)