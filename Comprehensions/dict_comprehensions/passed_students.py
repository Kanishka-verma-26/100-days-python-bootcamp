""" syntax : {new_key : new_value for (key, value) in dictionary.items() if test} """

students = {'kanishka': 49, 'Alex': 59, 'Beth': 11, 'Caroline': 68, 'Devansh': 93, 'Aashish': 17, 'Dave': 56, 'Anu': 67, 'Rashi': 19, 'Gursharan': 71, 'Eddie': 87, 'Paras': 88, 'Harshita': 71}
passed_students = {i:j for i,j in students.items() if j >= 60}

print(passed_students)