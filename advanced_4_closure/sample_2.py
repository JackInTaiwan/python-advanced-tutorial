def dog():
    height = 40
    
    def grow_up():
        height = height + 1

    return grow_up


if __name__ == "__main__":
    dog_grow_up = dog()
    dog_grow_up()
    # > UnboundLocalError: local variable 'height' referenced before assignment