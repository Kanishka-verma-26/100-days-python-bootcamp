print('''
           ,
          /(  ___________
         |  >:===========`
          )(
          ""
     ''')

auc = {}


def auction():
    name = input("What is your name : ")
    bid = int(input("What is your bid? : $"))
    auc[name] = bid


def main():
    print("Welcome to the secret auction program.")
    auction()
    n = input("Is there any other bidders? Types'y' or 'n' : ").lower()
    if n == "y":
        main()
    else:
        c = 0
        for i in auc:
            print(auc[i])

            if auc[i] > c:
                c = auc[i]
                winner = i
        print(f"The winner is {winner} with a bid of ${c}.")


main()