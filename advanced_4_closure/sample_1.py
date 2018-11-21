def dog():
    height = 40
    
    def profile():
        print("I'm a dog and my height is {}.".format(height))
        
    return profile



if __name__ == "__main__":
    dog_profile = dog()
    dog_profile()