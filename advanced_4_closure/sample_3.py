global x
x = 10

def add_x():
    x = x + 1



if __name__ == "__main__":
    add_x()
    # > UnboundLocalError: local variable 'x' referenced before assignment