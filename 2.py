def decor(func):
    def wrap():
        print("!!!!!!!!!!!!!!")
        func()
        print("!!!!!!!!!!!!!!")
    return wrap

@decor
def print_word():
    print("Hi")

print_word();
