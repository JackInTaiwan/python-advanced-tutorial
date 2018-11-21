def dog():
    height = 40
    
    def grow_up():
        nonlocal height
        height = height + 1
        
        def show_height():
            print("Thanks for making me growing up. I'm now {} meters !!!!".format(height))

        return show_height

    return grow_up


if __name__ == "__main__":
    dog_1_grow_up = dog()
    dog_1_grow_up()
    dog_1_grow_up()
    dog_1_grow_up()()
    # > Thanks for making me growing up. I'm now 43 meters !!!!

    dog_2_grow_up = dog()
    dog_2_grow_up()()
    # > Thanks for making me growing up. I'm now 41 meters !!!!