# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 16:20:33 2020

@author: k
"""

import pandas as pd


def get_word(lang,diff):
    """
    Parameters
    ----------
    lang : string (EN or ES)
        Should be "EN" for english or "ES" for spanish
    diff : number between 1 and 3
        Expects number 1-3 for difficulty rating

    Returns string of word 
    -------
    
    """
    pick_word = ""
    
    if (lang not in ["EN","ES"]) or (diff not in [1,2,3]):
        return pick_word
    else:
        full_word_list = pd.read_csv('word_list.csv')
        word_list = full_word_list[(full_word_list.Category == diff) & (full_word_list.Language==lang) ]
        word_row = word_list.sample()
        pick_word = word_row.iloc[0]['Word']
        return pick_word

def get_player_letter(letters):
    """
    Parameters
    --------
    letters: array
        array of letters already played in game

    Returns valid letter
    -------


    """
    player_letter = input("Please enter a letter to play: ")
    
    while (len(player_letter) > 1) or (not player_letter.isalpha()) or  (player_letter.lower() in letters):    
        print("You have entered an invaliid letter!")
        player_letter = input("Please enter a letter to play: ")
    
    return player_letter.lower()

def get_word_status(word,letter_list):
   
   word_array = list(word)
   current_word_status = [i if i in letter_list else "*" for i in word_array  ]
   return ("".join(current_word_status))

def play_hangman():
    """
    Main loop to play hangman game

    """
    #initialize all variables
    game_word = ""
    game_difficulty = ""
    game_language = ""
    played_letters =[]
    number_of_tries = 6
    
    
    #get inputs (Language, Difficulty)
    while (game_word == ""):
        game_difficulty = int(input("Enter game difficulty between and 1 (easy) and 3 (hard): "))
        game_language = input("Enter EN for english or ES for Spanish: ")
        game_word = get_word(game_language, game_difficulty)
    
    print(game_word)
    
    unsolved_letters = len(game_word)
    #get input (Avatar)
    
    #main game play
    #while loop to take input and check if game is over
    while (number_of_tries > 0) and (unsolved_letters > 0):
        print(get_word_status(game_word,played_letters))
        #show current game status
        new_letter = get_player_letter(played_letters) # get player input
        played_letters.append(new_letter)
        #update game status    
        if new_letter in game_word:
            unsolved_letters -= game_word.count(new_letter)
        else:
            number_of_tries -= 1     
    # end main while loop
    
    return game_word #temporary return
        