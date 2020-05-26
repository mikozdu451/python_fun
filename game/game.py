
running = True

def get_input():
    command = input(": ").split()
    verb_word = command[0]
    if verb_word in verb_dict:
        verb = verb_dict[verb_word]
    else:
        print("Unknown verb {}".format(verb_word))
        return

    if len(command) >= 2:
        name_word = command[1]
        print(verb(name_word))
    else:
        print(verb("null"))


def say(noun):
    return('You said "{}"'.format(noun))


def stop(noun):
    print("Thanks for playing!")
    return False


verb_dict = {"say": say, "stop": stop}

while running:
    get_input()

print("Shutting down...")
