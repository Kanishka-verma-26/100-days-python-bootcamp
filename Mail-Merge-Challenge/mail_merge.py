""" Given the names present in the 'invited_names.txt' file we need to generate invitation text file for all """


""" Method 1 """
# names = []
#
# with open("invited_names.txt") as data:
#     for i in data.read().split():
#         names.append(i)
# for i in names:
#     with open(f"letter_for_{i}.txt", mode="w") as file:
#         file.write(f"Dear {i},\n\nYou are invited to my birthday this Saturday.\n\nHope you can make it!\n\nKanishka")
#


""" Method 2 """

PlaceHolder = "[name]"

with open("invited_names.txt") as data:
    names = data.readlines()                # readlines convert lines of a file into array

with open("invited_names.txt") as data:
    letter_content = data.read()
    for name in names:
        stripped_name = name.strip()
        with open(f"letter_for_{stripped_name}.txt", mode="w") as file:
            file.write(f"Dear {stripped_name},\n\nYou are invited to my birthday this Saturday.\n\nHope you can make it!\n\nKanishka")