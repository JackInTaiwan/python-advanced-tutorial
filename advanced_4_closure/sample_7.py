### Use recursive lambda functions to define function with multiple arguments
add = lambda x: (lambda y: x + y)
print(add(3)(5))
# > 8


### Use normal function to do the same thing
def add(x, y):
    return x + y
print(add(3, 5))
# > 8