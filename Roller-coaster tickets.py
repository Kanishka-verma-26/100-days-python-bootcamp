print("Roller-coaster Ride!")
height = int(input("Enter your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Child tickets are $5.")
        bill += 5
    elif age <= 18:
        print("Youth tickets are $7.")
        bill += 7
    else:
        print("Adult tickets are $12.")
        bill += 12
    pic = input("Do you want a photo taken? Y or N.")
    if pic == "Y":
        bill += 3
    print(f"Your finnal bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride")