import random
alpha = 'abcdefghijklmnopqrstuwvxyz'
#i = 0
j = 1
new_string = ''
for i in range(10):
    x = random.randint(5,15)
    list = []
    while(j < x):
        #z = random.randint(1,2)
        y = random.randint(0,25)
        letter = alpha[y]
        #if(z == 2):
        #    letter = letter.upper()
        #print(letter)
        list.append(letter)

        j += 1
    #print("------------------")
    #print(''.join(list))
    print(''.join(list), file=open("output.txt","a"))
    #print("------------------")
    j = 0

#print(new_string)
print("Done")
