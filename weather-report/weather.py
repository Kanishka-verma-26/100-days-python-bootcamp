"""***************----------------- Printing temperature column using different ways -----------------***************"""





""" through the below code we will get each item as a row in a list"""

# with open("weather_data.csv") as file:
#     content = file.readlines()
#     print(content)

""" but its kind of difficult to work with a data which is in string format and separated with commas due to which
    it will need a lot of cleaning for actually extracting the each row"""


""" hence csv has its own library 'csv.reader' which will extract each row in a list"""

# import csv
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     print(data)                     # csv reader object
#
#     temperatures =[]
#     for i in data:
#         print(i)
#         if i[1] != 'temp':
#             temperatures.append(int(i[1]))
#     print(temperatures)


""" while csv is the inbuilt CSV reading and writing library, still so much of faff was involved in just simply getting
    a single column of data; but what will we do if we have more complex data with way more columns and rows and we want 
    to do more interesting things with it; its will be quite pain full to work with """


""" to overcome from above pain we use 'Pandas Library' """

""" Pandas Library is a python data analysis library i.e. super helpfull and powerfull to perform data analysis on 
    tabular data such as csv files """

""" Note: pandas represent whole 'dataframe' as (2-D array) representing each column as a single 'series' (1-D array); 
     refer : 'https://pandas.pydata.org/docs/reference/index.html' """

""" pip install pandas """

import pandas
data = pandas.read_csv("weather_data.csv")         # reading csv file using pandas
print(data)
print("\nTemperature column")
print(data['temp'])                             # printing the temperature column