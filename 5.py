word  = input()
i = 0
n = len(word)

while i < n:
    if word[i] in "aeiouy":
        print("vowel")
        i += 1
    else:
        print("consonant")
        i += 1
