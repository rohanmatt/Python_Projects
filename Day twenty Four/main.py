# file = open("data.txt")
# contents = file.read()
# print(contents)

with open("data.txt", "a") as file:
    file.write(" \n Python is amazing ")