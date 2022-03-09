def game():
    print("""
  ___  _  _  ____  ____  ____    ____  _  _  ____    __ _  _  _  _  _  ____  ____  ____ 
 / __)/ )( \(  __)/ ___)/ ___)  (_  _)/ )( \(  __)  (  ( \/ )( \( \/ )(  _ \(  __)(  _ \
( (_ \) \/ ( ) _) \___ \\___ \    )(  ) __ ( ) _)   /    /) \/ (/ \/ \ ) _ ( ) _)  )   /
 \___/\____/(____)(____/(____/   (__) \_)(_/(____)  \_)__)\____/\_)(_/(____/(____)(__\_)""")
    import random
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    n = random.randint(1, 100)
    # diff = input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()
    diff = 'hard'
    if diff == 'easy':
        attempts(10, n)
    else:
        attempts(5, n)
    again = input("This repl is excited, run again ? (y/n) :").lower()
    if again == "y":
        game()
    else:
        print("Thankyou for playing ")
        return


def attempts(x, n):
    for i in range(x):
        print("You have", x - i, " attempts remaining to guess the number. ")
        z = int(input())
        if z == n:
            print("correct, you won")
            return
        elif z < n:
            print("Too low")
        else:
            print("Too high")
    print("You Lose! ")


game()