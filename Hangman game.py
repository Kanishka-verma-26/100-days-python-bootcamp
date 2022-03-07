print("Hangman Game!")

print("""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       """)

hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''',
           '''
             +---+
             |   |
             O   |
                 |
                 |
                 |
           =========''',
           '''
             +---+
             |   |
             O   |
             |   |
                 |
                 |
           =========''',
           '''
             +---+
             |   |
             O   |
            /|   |
                 |
                 |
           =========''',
           '''
             +---+
             |   |
             O   |
            /|\  |
                 |
                 |
           =========''',
           '''
             +---+
             |   |
             O   |
            /|\  |
            /    |
                 |
           =========''',
           '''
             +---+
             |   |
             O   |
            /|\  |
            / \  |
                 |
           =========''']

display = []


def hang(c=6):
    print(hangman[-c - 1])
    if c == 0:
        print("You Lose")
        return
    if v.count("_ ") > 0:
        z = input("Guess a letter : ").lower()
        if z in display:
            print("You already guessed this number ")
            print("".join(v))
            hang(c)
        else:
            display.append(z)
            if z in a:
                print("Correct guess, you have", c - 1, "lives left")
                for i in range(len(a)):
                    if a[i] == z:
                        v[i] = z
                print("".join(v))
                hang(c)

            else:
                print("Wrong guess, try again!")
                print("you have", c - 1, "lives left")
                print("".join(v))
                hang(c=c - 1)
    else:
        print("WoOHoOoo! You Win")


import random

li = ["advark", "hangman", "cartoon", "baboon", "camel", "paparazzi"]

# randomply choosing a word
a = random.choice(li)
print(a)

# blank spaces for the chosen word
v = ["_ " for i in range(len(a))]
print("".join(v))
hang()