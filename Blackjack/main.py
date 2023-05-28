############### Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1
## Cards are not removed from the deck as they are drawn.

import os
import platform
import random
from art import logo


deck = {
    "Ace": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10
}

user_cards = []
computer_cards = []
choice = ""
play_again = "y"

def clear():
    if platform.system() == "Linux":
        os.system('clear')
    elif platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def deal_card():
  card = random.choice(list(deck))
  return card


def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)


def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"
  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def play_game():

  print(logo)

  user_cards = []
  computer_cards = []
  user_cards_names = []
  computer_cards_names = []
  is_game_over = False

  for _ in range(2):
    user_card = deal_card()
    computer_card = deal_card()
    user_cards_names.append(user_card)
    computer_cards_names.append(computer_card)
    user_cards.append(deck[user_card])
    computer_cards.append(deck[computer_card])


  while not is_game_over:
    computer_score = calculate_score(computer_cards)
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Your cards: {user_cards_names}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards_names[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        user_card = deal_card()
        user_cards_names.append(user_card)
        user_cards.append(deck[user_card])
      else:
        is_game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_card = deal_card()
    computer_cards_names.append(computer_card)
    computer_cards.append(deck[computer_card])
    computer_score = calculate_score(computer_cards)

  print(f"   Your final hand: {user_cards_names}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards_names}, final score: {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()
