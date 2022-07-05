try:
    file = open("example.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("example.txt", "w")
    file.write("i am awesome")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
# finally:
#     raise TypeError("This is an error that i caused.")