import random
from ASCII_ART import logo
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # create a function to deal cards


def add(totals):
    total_sum = 0
    for total in totals:
        total_sum += total  # BlackJack if starting 2 cards total sum is equal to 21 return 0
    return total_sum


def starting_cards(number):  # add definition
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
    total_user += add(user_cards)  # Use sum function
    total_computer += add(computer_cards)

    print(f"Your cards: {user_cards}, current score: {total_user}")
    print(f"Your cards: {computer_cards}, current score: {total_computer}")  # debugg

    restart = True
    while restart:  # if player score is already 21 game ends??
        var_another_card = input("Type 'y' to get another card, type 'n' to pass: n ").lower()

        if total_computer > 21:
            cards[1] = 1  # if user score is equal to 21 change Ace to var 1

        if total_computer < 17:  # use while loop
            computer_cards.append(starting_cards(1))
            total_computer += computer_cards[-1]

        if var_another_card == "y":
            user_cards.append(starting_cards(1))
            total_user += user_cards[-1]
            print(f"Your cards: {user_cards}, current score: {total_user}")
            if total_user >= 22:  # computer and player gets blackjack game ends
                print("\n")
                print(f"Your cards: {user_cards}, current score: {total_user}")
                print(f"Computer's final hand: {computer_cards}, final score: {total_computer}")
                print("You lose 😭")
                restart = False

        if var_another_card == "n":
            print("\n")
            print(f"Your cards: {user_cards}, your final score: {total_user}")
            print(f"Computer's final hand: {computer_cards}, final score: {total_computer}")
            if total_computer >= 22 and total_user >= 22:
                print("You both lose")
            elif total_computer >= 22:
                print("You win 😃")
            elif total_user == total_computer:
                print("It is a draw")
            elif total_user > total_computer:  # create a function that compares
                print("You win 😃")
            elif total_user < total_computer:
                print("You lose 😭")
            restart = False
    game_restart = True
    while game_restart:
        var_user_choice = input("Restart the game? Type 'y' or 'n': ").lower()
        if var_user_choice == "y":
            start()
            game_restart = False
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')
        else:
            game_restart = False


var_user = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
if var_user == "y":
    start()
