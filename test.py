def print_start_and_end(func):
    def wrapper():
        print("---START---")
        func()
        print("---END---")

    return wrapper


@print_start_and_end
def introduce():
    print("I am Michael")


introduce()
