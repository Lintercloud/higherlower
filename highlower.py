# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 17:03:18 2020

@author: Linter
"""

from game_data import data
from art import logo, vs
import random


def massage(guess_a, guess_b):
    print("Compare A:", guess_a["name"], ",", guess_a["description"], ",", guess_a["country"])
    print(vs)
    print("Against B:", guess_b["name"], ",", guess_b["description"], ",", guess_b["country"])


def random_guess(data, guess_a):   
    guess_b = random.choice(data)
    while guess_b == guess_a:
        guess_b = random.choice(data)
    return guess_b    


def compard(guess_a, guess_b, count, start_game):
    answer = input("Who has more follwers? type'a' or 'b': ")
    if guess_a["follower_count"] > guess_b["follower_count"] and answer == "a":
        count +=1
        print(f"you got the answer,corrent socre is {count}\n")
    elif guess_a["follower_count"] < guess_b["follower_count"] and answer == "b":    
        count +=1
        guess_a = guess_b
        print(f"you got the answer,corrent socre is {count}\n")
    else:
        print(f"Sorry, you get wrong,your score is {count}")
        start_game = False 
    return guess_a, count, start_game     


start_game = True
guess_a = random.choice(data)
count = 0
while start_game:
    print(logo)   
    guess_b = random_guess(data, guess_a)
    massage(guess_a, guess_b)
    guess_a, count, start_game = compard(guess_a, guess_b, count, start_game)



