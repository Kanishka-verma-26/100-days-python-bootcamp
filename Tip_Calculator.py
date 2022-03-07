print("Tip Calculator!")
price = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would  you like to give? 10, 12, or 15? "))
to_people = int(input("How many people to split the bill? "))

to_price = ((price*(tip/100)+price)/to_people)
to_price = round(to_price,2)
# to_price = "{:2f}".format(to_price)
print("Each person should pay: $"+str(to_price))