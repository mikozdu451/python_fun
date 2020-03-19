samo = "aeiouy"
x = input("wprowadź komunikat: ")
new = ""

for char in x:
    if char.lower() not in samo:
        new += char
        print("New =", new)
print("Final new =", new)
input("\n\nEnd")
