import pandas as pd
import unicodedata

used_word_list = list() #initialize as global variable
 
def display_hangman(tries):
    stages = [  # final state: cat lose the fish
               """
    /\\_,/\
   / _  _ |      ,--.
  (   T   )  ,-' ,-'
   \  _ _/-._(  (
   /          `.`.   
  |         _     |
   \ \ ,  /     | |      _
    || |-_\__    /   ___/ \________________________________________________________________________________________________
   ((_/`(____,-'        \_/

                """,
                # get closer
                """
               |\__/|
              (_ ^_^ )  
         _     )    (                           ____   
        ((    /      \     (((             ____/..  \
         \(   )  | || |     )))        _   v       \/     _
          '__'  '_''_',    >+++°>_____/ \___\_______|____/ \______________________________________________________________
                                      \_/                \_/ 
                """,
                # get closer
                """
               |\__/|
              (_ ^_^ )  
         _     )    (                                    ____   
        ((    /      \     (((                      ____/..  \
         \(   )  | || |     )))                 _   v       \/     _
          '__'  '_''_',    >+++°>______________/ \___\_______|____/ \_____________________________________________________
                                               \_/                \_/ 

                """,
                # get closer
                """

               |\__/|
              (_ ^_^ )  
         _     )    (                                              ____   
        ((    /      \     (((                                ____/..  \
         \(   )  | || |     )))                           _   v       \/     _
          '__'  '_''_',    >+++°>________________________/ \___\_______|____/ \___________________________________________ 
                                                         \_/                \_/ 

                """,
                # get closer
                """
               |\__/|
              (_ ^_^ )  
         _     )    (                                                               ____   
        ((    /      \     (((                                                 ____/..  \
         \(   )  | || |     )))                                            _   v       \/     _
          '__'  '_''_',    >+++°>_________________________________________/ \___\_______|____/ \__________________________ 
                                                                          \_/                \_/ 
    
                """,
                # hdog apears
                """
               |\__/|
              (_ ^_^ )  
         _     )    (                                                                                  ____   
        ((    /      \     (((                                                                     ___/..  \
         \(   )  | || |     )))                                                                _   v       \/     _
          '__'  '_''_',    >+++°>_____________________________________________________________/ \___\_______|____/ \______ 
                                                                                              \_/                \_/ 
                """,
                # initial empty state
                """
               |\__/|
              (_ ^_^ )  
         _     )    (
        ((    /      \     (((
         \(   )  | || |     )))
          '__'  '_''_',    >+++°>
    
                """
    ]
    return stages[tries]

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
    
    if (lang not in ["EN","ES"]) or (diff not in ["1","2","3"]):
        return pick_word
    else:
        full_word_list = pd.read_csv('word_list.csv')
        word_list = full_word_list[(full_word_list.Category == int(diff)) & (full_word_list.Language==lang) ]
        word_row = word_list.sample()
        pick_word = word_row.iloc[0]['Word']
        while pick_word in used_word_list:
            word_list = full_word_list[(full_word_list.Category == diff) & (full_word_list.Language==lang) ]
            word_row = word_list.sample()
            pick_word = word_row.iloc[0]['Word']
                
        
        return pick_word
        #return "cínción"

def remove_accent(ltr):
    return unicodedata.normalize("NFKD",ltr).encode("ASCII","ignore").decode("ascii")

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
   current_word_status = [i if (i in letter_list) or (remove_accent(i) in letter_list)  else "*" for i in word_array  ]
   return ("".join(current_word_status))

def check_letter(word,letter):
    return any([letter == remove_accent(i) or i == letter for i in word ])

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
        game_difficulty = input("Enter game difficulty between and 1 (easy) and 3 (hard): ")
        game_language = input("Enter EN for english or ES for Spanish: ")
        game_word = get_word(game_language, game_difficulty)
        
    print(display_hangman(number_of_tries))
    unsolved_letters = len(game_word)
    #get input (Avatar)
    #main game play
    
    #while loop to take input and check if game is over
    while (number_of_tries > 0) and (unsolved_letters > 0):
        display_word = get_word_status(game_word,played_letters)
        print(display_word)
        #show current game status
        new_letter = get_player_letter(played_letters) # get player input
        print(new_letter)
        
        played_letters.append(new_letter)
        #update game status    
        if check_letter(game_word, new_letter):
            display_word = get_word_status(game_word,played_letters)
            unsolved_letters = display_word.count("*")
        else:
            number_of_tries -= 1
        
        print(display_hangman(number_of_tries))     
        print(" ".join(played_letters))
        # end main while loop
    
    print(game_word)
    result = "You Won!" if number_of_tries > 0 else "You Lost!!!!"
    print(result)
    return [game_word, result]
   
def multi_gameplay():
    used_word_list = list()
    streak = [0,0]
    hangman_results = play_hangman()
    used_word_list.append(hangman_results[0])
    game_result = hangman_results[1]
    if game_result == "You Won!":
        streak[0] += 1
    else:
        streak[1] += 1
    while input("Play Again? (Y/N) ").upper() == "Y":
        hangman_results = play_hangman()
        game_word = hangman_results[0]
        game_result = hangman_results[1]
        used_word_list.append(game_word)
        if game_result == "You Won!":
            streak[0] += 1
        else:
            streak[1] += 1
    print(used_word_list)
    print(f"Wins: {streak[0]} | Losses: {streak[1]} ")