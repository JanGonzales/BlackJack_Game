import random
from ASCII_ART import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def add(totals):
    total_sum = 0
    for total in totals:
        total_sum += total
    return total_sum


def starting_cards(number):
    for card in range(0, number):
        random_cards = random.choice(cards)
        return random_cards


def start():
    print(logo)
    user_cards = []
    computer_cards = []
    total_user = 0
    total_computer = 0

    for card in range(0, 2):
        user_cards.append(starting_cards(2))
        computer_cards.append(starting_cards(2))
    total_user += add(user_cards)
    total_computer += add(computer_cards)

    print(f"Your cards: {user_cards}, current score: {total_user}")
    print(f"Your cards: {computer_cards}, current score: {total_computer}")  ##debugg

    restart = True
    while restart:
        var_another_card = input("Type 'y' to get another card, type 'n' to pass: n ").lower()

        if total_computer < 17:
            computer_cards.append(starting_cards(1))
            total_computer += computer_cards[-1]

        if var_another_card == "y":
            user_cards.append(starting_cards(1))
            total_user += user_cards[-1]
            print(f"Your cards: {user_cards}, current score: {total_user}")
            print(f"Computer's hand: {computer_cards}, computer score: {total_computer}")  ##debug
            if total_user >= 22:
                print("\n")
                print(f"Your cards: {user_cards}, current score: {total_user}")
                print(f"Computer's final hand: {computer_cards}, final score: {total_computer}")
                print("You lose 😭")
                restart = False

        elif var_another_card == "n":
            print("\n")
            print(f"Your cards: {user_cards}, your final score: {total_user}")
            print(f"Computer's final hand: {computer_cards}, final score: {total_computer}")
            if total_user > total_computer:
                print("You win 😃")
            elif total_user < total_computer:
                print("You lose 😭")
            elif total_user == total_computer:
                print("It is a draw")
            restart = False



    # if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":



var_user = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
if var_user == "y":
    start()
