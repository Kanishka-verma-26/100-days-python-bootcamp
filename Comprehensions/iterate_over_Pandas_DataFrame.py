student_dict = {
    'student':['kanishka','rashi','harshita'],
    'score':[56,76,44]
}

""" looping through dictionary """

for key,val in student_dict.items():
    print(val)


import pandas
student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)


""" looping through dataframe """

# # the below method is not particularly useful because its basically just looping through name of the column and then
# # the data inside each column

# for key,val in student_data_frame.items():
#     print(val)


""" to overcome above problem pandas has a inbuilt loop method called 'iterrows()' it allows us to loop through each of the 
    rows of dataframe rather than each of the columns """

for (index,row) in student_data_frame.iterrows():
    print(row)
    print(row.student)
    print(row.score)
    print()