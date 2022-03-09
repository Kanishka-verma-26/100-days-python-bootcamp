import random


def calc_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def game():
    print("""
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                       _/ |                
                      |__/           
""")
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = []
    comp_cards = []
    for i in range(2):
        user_cards.append(random.choice(cards))
        comp_cards.append(random.choice(cards))

    is_game_over = False

    while not is_game_over:

        print("your cards ", user_cards)
        print("comp cards ", comp_cards[0])
        us_sc = calc_score(user_cards)
        co_sc = calc_score(comp_cards)
        print("us ", us_sc)
        print("co ", co_sc)

        if us_sc > 21 or us_sc == 0 or co_sc == 0:
            is_game_over = True
        else:
            z = input("Type 'y' to get another card, else 'n' to pass: ").lower()
            if z == 'y':
                user_cards.append(random.choice(cards))
                us_sc = calc_score(user_cards)
            else:
                is_game_over = True

    while co_sc != 0 and co_sc < 17:
        comp_cards.append(random.choice(cards))
        co_sc = calc_score(comp_cards)
    print(f" Your final hand: {user_cards}, final score: {us_sc}")
    print(f" Computer's final hand: {comp_cards}, final score: {co_sc}")
    print(compare(us_sc, co_sc))
    ip = input("Do you want to play a game of Blackjack? Type 'y/n' : ").lower()
    if ip == 'y':
        game()
    else:
        print("Thankyou for playing")
        return


def compare(us_sc, co_sc):
    if us_sc == co_sc:
        return "Draw"
    elif co_sc == 0:
        return "Lose, opponent has Blackjack"
    elif us_sc == 0:
        return "Win with a Blackjack"
    elif us_sc > 21:
        return "You went over, you lose"
    elif co_sc > 21:
        return "Opponent went over, you win"
    elif us_sc > co_sc:
        return "You Win"
    else:
        return "You Lose"


game()