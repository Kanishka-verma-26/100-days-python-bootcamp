from turtle import Turtle,Screen

# # PrettyTable
""" A simple Python library for easily displaying tabular data in a visually appealing ASCII table format
    installation : pip install -U prettytable
 """


from prettytable import PrettyTable
table = PrettyTable()
print("empty table :")                # empty table
print(table)
print()
table.field_names = ["Pokemon Name", "Tyoe"]        # adding all rows at once
table.add_rows(
    [
        ["Pikachu", 'Electric'],
        ["Squirtle", 'Water'],
        ["Charmander", 'Fire'],
    ]
)
print("pokemon table :")
print(table)
print()

table.align = 'l'                   # aligning table content to left
print("pokemon table with left alignment :")
print(table)
