import random

i = 1
counter_one = 1


print("Let's play a game, i choose a number you have ten times")

i = random.randint(1,100)
x = int(input())

while i != x:
    
    if x > i:
        print("Try smaller number")

    elif x < i:
        print("Try bigger number")

    x = int(input())
    counter_one += 1

print("You geuessed it in ", counter_one, " tries, and the number indeed was ", i,"!")
input("\n\nEnter to end program")
