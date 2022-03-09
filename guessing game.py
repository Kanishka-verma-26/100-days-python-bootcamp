import random

a = {"kim": 50, "khloe": 10, "kylie": 60, "kourtney": 20, "kendall": 48, "broddy": 2.5, "rob": 5, "burt": 3}
b = {"carry": 50, "bb": 60, "ashish": 55, "harsh": 45, "OMG": 20, "boho": 30, "quirky": 33, "saima": 40}


def game(c=0):
    print("""
 ██████╗ ██╗   ██╗███████╗███████╗███████╗██╗███╗   ██╗ ██████╗ 
██╔════╝ ██║   ██║██╔════╝██╔════╝██╔════╝██║████╗  ██║██╔════╝ 
██║  ███╗██║   ██║█████╗  ███████╗███████╗██║██╔██╗ ██║██║  ███╗
██║   ██║██║   ██║██╔══╝  ╚════██║╚════██║██║██║╚██╗██║██║   ██║
╚██████╔╝╚██████╔╝███████╗███████║███████║██║██║ ╚████║╚██████╔╝
 ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
    """)
    print("""
 ██████╗  █████╗ ███╗   ███╗███████╗
██╔════╝ ██╔══██╗████╗ ████║██╔════╝
██║  ███╗███████║██╔████╔██║█████╗  
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
    """)
    res1 = key, val = random.choice(list(a.items()))
    res2 = key, val = random.choice(list(b.items()))
    print(res1[0], res2[0])
    print("Compare A:", res1[0])
    print("""
___  ________
\  \/ /  ___/
 \   /\___ \ 
  \_//____  >
          \/ """)
    print("Compare B:", res2[0])
    s = input("Who has more followers? Type'A' or 'B': ").lower()
    guess(c, s, res1, res2)
    z = input("Doo you wanna play again? (y/n) : ")
    if z == 'y':
        game()
    else:
        print("Thankyou for investing your precious time on this game")
        return


def guess(c, s, res1, res2):
    if s == "a":
        if res1[1] > res2[1]:
            print("yeshshs! you guessed it correct")
            game(c + 1)
        else:
            print(f"Wrong guess!, you guessed {c} correct answers")
    else:
        if res1[1] < res2[1]:
            print("yeshshs! you guessed it correct")
            game(c + 1)
        else:
            print(f"Wrong guess!, you guessed {c} correct answers")


game()