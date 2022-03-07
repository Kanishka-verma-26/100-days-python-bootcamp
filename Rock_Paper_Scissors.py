import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


def choice(a):
    if a == 0:
        return rock, "Rock"
    elif a == 1:
        return paper, "Paper"
    else:
        return scissor, "Scissors"


def rec():
    a = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors : "))
    print("Your's choice : ")
    z = choice(a)
    print(z[0], z[1])
    li = {1: rock, 2: paper, 3: scissor}
    print("Computer's choice : ")
    res = random.choice(list(li.keys()))
    w = choice(res)
    print(w[0], w[1])

    if z[1] == w[1]:
        print("It's a draw, try again")
        rec()
    elif z[1] == "Rock" and w[1] == "Paper":
        print("You Lose")
    elif z[1] == "Paper" and w[1] == "Scissors":
        print("You Lose")
    elif z[1] == "Scissors" and w[1] == "Rock":
        print("You Lose")
    else:
        print("WoOHoOOoo! You win")


rec()