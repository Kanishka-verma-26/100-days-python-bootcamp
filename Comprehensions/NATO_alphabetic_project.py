import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
dict = {row.letter:row.code for (index,row) in data.iterrows()}

name = input("What's your name ? : ").upper()
op_list = [dict[letter] for letter in name]
print(op_list)


# for i in name:
#     for (index,row) in data.iterrows():
#         if i == row.letter:
#             dict[row.letter] = row.code
# print(dict)