PLACEHOLDER = "[name]"


with open("./Input/Names/invited_names.txt") as file_name:
    names = file_name.readlines()

with open("./Input/Letters/starting_letter.txt") as file_letter:
    content = file_letter.read()
    for name in names:
        format_name = name.strip()
        new_letter = content.replace(PLACEHOLDER, format_name)
        with open(f"./Output/ReadyToSend/letter_for_{format_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)

