""" csv dataframe to html """
import pandas
data_csv = pandas.read_csv("weather_data.csv")
data_html = data_csv.to_html()
print(data_html)


""" csv dataframe to dictionary """
data_dict = data_csv.to_dict()
print("\ndict :",data_dict)


""" csv series to list """
data_list = data_csv['temp'].to_list()
print("\nlist :",data_list)


""" average of temperatures """
# avg = sum(data_list)/len(data_list)
# print(avg)

# # or

print("\nmean :",data_csv['temp'].mean())


""" maximum temperature """
print("\nmax temp :",data_csv['temp'].max())


""" printing row data of monday """
print(data_csv[data_csv.day=='Monday'])

# # or

# print(data_csv[data_csv['day']=='Monday'])


""" printing row data of maximum temperature """
max_temp = data_csv.temp.max()
print()
print(data_csv[data_csv.temp == max_temp])


""" printing temperature condition of Monday """
monday = data_csv[data_csv.day=='Monday']
print("\nMonday's condition :", monday.condition)


""" Mondays temp in fahrenheit """
print(monday.temp*(9/5)+32)
print()


""" creating database/csv from scratch """
data_dict = {
    "students":["Amy","James","Angela"],
    "scores":[76,56,43]
}
data=pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")                 # this will create a new csv file as 'new_data.csv' donot exist



""" converting the '2018_Squirrel_Data.csv' to new 'squirrel_count.csv' file 
which will store the count of squirrels based on their colors """

squirrel_data = pandas.read_csv("2018_Squirrel_Data.csv")
# black_c = 0
# grey_c = 0
# red_c = 0

# for color in squirrel_data['Primary Fur Color']:
#     if (color) == "Gray":
#         grey_c+=1
#     elif color == "Cinnamon":
#         red_c+=1
#     elif color == "Black":
#         black_c+=1

grey_c = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
red_c = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_c = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

squirrel_count = {
    "Fur Color":['grey','red','black'],
    'Count':[grey_c, red_c, black_c]
}
squirrel = pandas.DataFrame(squirrel_count)
squirrel.to_csv("squirrel_count.csv")