"""
Function : is group of statements.
functions is declare ones and use many times as per the need.
we can call function anywhere in our program.
Advantage: cod reusability
 Three types of function:-
        1. Built - in - function  ex. print, input, eval etc.
        2. Higher order function ex. filter(), map(), and reduce()
        3. user defined function.
            these are the function developed by users according to business requirements.
            using def keyword.
        4. Recursive Function : function called itself.


# positional arguments . sequences matter
def sample(a, b):
    c = a + b
    return print(a, b)


sample(20, 10)



# keyword Arguments : position does not matter
def sample(name, age, sal):
    print(f"name: {name}, age: {age}, sal: {sal}")


sample(age= 18, name= "shubham", sal= 201135)




# combination of positional and keyword argument

def fun(name, age, sal):
    print(f"name: {name}, age: {age}, sal: {sal}")


fun("vishal", age=18, sal= 12000)




# default arguments

def sample(name, sal, age=18):
    print(f"name: {name}, age: {age}, sal: {sal}")


sample("vishal", 10000, 45)




# variable length arguments(*args, **kwargs)

def sample(*args):   # returns tuple as output
    print(args)


sample(1)
sample()
sample(10, 20, 40, 56, 45)
sample(145524, 57)




def kw(**kwargs):  # returns dict. as output
    print(kwargs)


kw(name="vishal")
kw(name="shubham", age=18)
kw(name="xyz", place="pune", pin=45412)





# Recursive function

def fact(n):
    if n == 0:
        result = 1
    else:
        result = n * fact(n - 1)

    return result


print(fact(5))


# Lambda Function :  nameless function
function without a name is an anonymous function ,
this function used to instance (one tme usage)

lambda function:
    lambda(parameter : expression)

c = lambda x, y, z: (x + y) + (y + z)
print(c(3, 4, 12))

# default return statement.
# higher order functions
# its needs a function as arguments i.e. is called higher order function

# filter:
s = [10, 20, 31, 41, 44, 21, 24, 23]
f = filter(lambda x: x % 2 == 0, s)
print(list(f))

# map ():
s = [10, 20, 31, 41, 44, 21, 24, 23]
f = map(lambda x: x + 10, s)
print(list(f))


# reduce():
from functools import reduce as rd
s = [10, 20, 31, 41, 44, 21, 24, 23]
f = rd(lambda x, y: x + y, s)
print(f)




# closure:
def outer():
    x = 12

    def inner():
        y = 10
        result = x + y
        return result

    return inner


o = outer()
print(o())

"""








