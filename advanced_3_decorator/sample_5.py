import time


def print_func_name(time):
    def decorator(func):
        def warp():
            print("Now use function '{}'".format(func.__name__))
            print("Now Unix time is {}.".format(int(time)))
            func()
        return warp
    return decorator


@print_func_name(time=(time.time()))
def dog_bark():
    print("Bark !!!")



if __name__ == "__main__":
    dog_bark()
    # > Now use function 'dog_bark'
    # > Now Unix time is 1541296864.2953653.
    # > Bark !!!