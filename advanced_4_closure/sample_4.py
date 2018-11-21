def dog():
    height = 40
    
    def grow_up():
        nonlocal height
        height = height + 1
        print("Thanks for making me growing up. I'm now {} meters !!!!".format(height))

    return grow_up


if __name__ == "__main__":
    dog_grow_up = dog()
    dog_grow_up()
    # > Thanks for making me growing up. I'm now 41 meters !!!!