def addi(n1, n2):
    return n1 + n2


def subt(n1, n2):
    return n1 - n2


def mult(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


def main_1():
    print("""
           _            _       _             
          | |          | |     | |            
  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
| (_| (_| | | (__| |_| | | (_| | || (_) | |   
 \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                            """)
    print("""
     _____________________
    |  _________________  |
    | | JO           0. | |
    | |_________________| |
    |  ___ ___ ___   ___  |
    | | 7 | 8 | 9 | | + | |
    | |___|___|___| |___| |
    | | 4 | 5 | 6 | | - | |
    | |___|___|___| |___| |
    | | 1 | 2 | 3 | | x | |
    | |___|___|___| |___| |
    | | . | 0 | = | | / | |
    | |___|___|___| |___| |
    |_____________________|
    """)
    n1 = float(input("What is the first number? : "))
    main_2(n1)


def main_2(n1):
    operations = {"+": addi, "-": subt, "*": mult, "/": div}
    n2 = float(input("What is the second number? : "))
    op = input("Which operation do you want to perform? (+ - * /) : ")
    calc_func = operations[op]
    ans = calc_func(n1, n2)
    print(f"{n1} {op} {n2} = {ans}")
    z = input(
        f"Type 'y' to continue calculation with '{ans}', or type 'n' to exit., or type 's' to restart again : ").lower()
    if z == 'y':
        main_2(ans)
    elif z == "n":
        print("Thankyou for coming")
        return
    else:
        main_1()


main_1()