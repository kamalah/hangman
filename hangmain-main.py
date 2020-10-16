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

def play_hangman():
    """
    Main loop to play hangman game

    """
    #get inputs (Language, Difficulty, Avatar)
    game_word = ""
    game_difficulty = ""
    game_language = ""
    while (game_word == ""):
        game_difficulty = int(input("Enter game difficulty between and 1 (easy) and 3 (hard): "))
        game_language = input("Enter EN for english or ES for Spanish: ")
        game_word = get_word(game_language, game_difficulty)
    
    #main game play
    #while loop to take input and check if game is over
    
    
    return game_word
        