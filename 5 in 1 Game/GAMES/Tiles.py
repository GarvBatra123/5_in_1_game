#var = variable
import random 
import sys
import time   


def len_and_shuffling_of_matrix(original_state):
    """
    This function generates a list (of numbers from (1-8) and a whitespace) in a random order and shuffles it

    Parameters
    ----------
    original_state: list
        it is an empty list in which this function will append the numbers generated in random order

    Returns
    -------
    original_state: list
        it stores the numbers generated in random order

    """
    count = 0
       
    original_state = random.sample(range(1,9), (8)) # to make sure that there is no duplicate number in the matrix 
    #oprint(original_state)
    original_state.append(' ') #add empty strings to the list (that will be replaced )
    for i in range(9):
        original_state[i] = str(original_state[i]) #convert each instance of list to a string to easily compare in next line of code
        
             
    random.shuffle(original_state) # shuffle list to reduce chances of ' ' always being the last index of the matrix
    return original_state



def get_list_of_numbers_to_move(original_state, *list_of_possible_moves):
    """
    This function stores all the possible moves the player can move each time, in a list, to help validate whether each move is valid or not

    Parameters
    ----------
    original_state: List 
        it is the randomised list  of numbers 
    list_of_possible_moves: list
        it is the list of possible moves the player can move

    Returns
    -------
    lst_of_numbers_that_can_be_moved: list
        this is a list of the possible moves the player can move

    """


    lst_of_numbers_that_can_be_moved = []
    for i in list_of_possible_moves:
        lst_of_numbers_that_can_be_moved.append(original_state[i])
    return lst_of_numbers_that_can_be_moved

def printing_randomisedMatrix(original_state):
    """
    This function asks the player for input and validates it whether the input is valid or invalid. After that it prints the list of randomised numbers (original_state) as a 3x3 matrix
    
    parameters
    ----------
    original_state: List
        it is the randomised list  of numbers that will be printed out    

    """
    
    count_of_loops = 0

    lst_of_praises = ['Well done!','Good job!','Bingo!', 'Great work!','Excellent!','Splendid!'] #praises that will be auto-generated if a player guesses the number correctly
    #print(original_state) #troubleshoot
    print('\n')
    #allowed list of characters to be input
    allowed_character_list=["1","2","3","4","5","6","7","8"]
    while original_state[0:8] != (sorted(original_state))[1:9]:
        if count_of_loops > 0:
            lst_of_numbers_that_can_be_moved = []
            position_of_emptySpot = original_state.index(' ')
            position_of_number_on_right_of_emptySpot = (position_of_emptySpot+1) #index value of number next to blank
            position_of_number_on_left_of_emptySpot = (position_of_emptySpot-1)#index value of number before blank
            position_of_number_above_emptySpot = (position_of_emptySpot - 3)#index value of number above blank 
            position_of_number_below_emptySpot = (position_of_emptySpot + 3)#index value of number below blank
            
            #append the only numbers that can be moved
            if position_of_emptySpot == 0: # if ' ' is in first position on right corner
                lst_of_numbers_that_can_be_moved=get_list_of_numbers_to_move(original_state, position_of_number_on_right_of_emptySpot, 
                    position_of_number_below_emptySpot) # if empty spot is at index0, numbers he can move are to the right and below the blank
               
            elif position_of_emptySpot == 1:
                lst_of_numbers_that_can_be_moved=get_list_of_numbers_to_move(original_state, position_of_number_on_right_of_emptySpot,
                    position_of_number_below_emptySpot,position_of_number_on_left_of_emptySpot)  # if empty spot is at index1, numbers he can move are to the right, below and to the left of the blank


            elif position_of_emptySpot == 2:
                
                lst_of_numbers_that_can_be_moved=get_list_of_numbers_to_move(original_state,position_of_number_below_emptySpot,
                    position_of_number_on_left_of_emptySpot)  # if empty spot is at index2, numbers he can move are to the left and below the blank

            elif position_of_emptySpot == 3:
                lst_of_numbers_that_can_be_moved=get_list_of_numbers_to_move(original_state,position_of_number_on_right_of_emptySpot,
                    position_of_number_below_emptySpot,position_of_number_above_emptySpot) # if empty spot is at index1, numbers he can move are to the right and below the blank

            elif position_of_emptySpot == 4:
            
                lst_of_numbers_that_can_be_moved=get_list_of_numbers_to_move(original_state,position_of_number_on_right_of_emptySpot,
                    position_of_number_on_left_of_emptySpot, position_of_number_above_emptySpot,position_of_number_below_emptySpot) 

            elif position_of_emptySpot == 5:
                lst_of_numbers_that_can_be_moved=get_list_of_numbers_to_move(original_state,position_of_number_on_left_of_emptySpot,
                    position_of_number_above_emptySpot, position_of_number_below_emptySpot)

            elif position_of_emptySpot == 6:
                lst_of_numbers_that_can_be_moved=get_list_of_numbers_to_move(original_state,position_of_number_above_emptySpot,
                    position_of_number_on_right_of_emptySpot)

            elif position_of_emptySpot == 7:
                lst_of_numbers_that_can_be_moved=get_list_of_numbers_to_move(original_state, position_of_number_on_right_of_emptySpot,
                    position_of_number_on_left_of_emptySpot,position_of_number_above_emptySpot)
              
            elif position_of_emptySpot == 8:
                lst_of_numbers_that_can_be_moved=get_list_of_numbers_to_move(original_state,position_of_number_on_left_of_emptySpot,
                    position_of_number_above_emptySpot)
            
            while True:
                number_that_player_wants_to_move = input('WHAT NUMBER DO YOU WANT TO MOVE: ') 
                if number_that_player_wants_to_move == 'quit':
                    quit_statemet = ('                    ******************QUITTING FROM TILES******************** \n********************THANK YOU FOR PLAYING TILES. PLEASE CHECK OUR OTHER GAMES********************')
                    for characters in quit_statemet:
                        sys.stdout.write(characters)
                        time.sleep(0.003)
                    sys.exit()

                if number_that_player_wants_to_move not in allowed_character_list: #check if player's move is in range(1-9)
                    for character in (f'SORRY, YOU CANNOT ENTER "{number_that_player_wants_to_move}" AS IT IS NOT IN RANGE FROM 1-8; PLEASE ENTER A NUMBER IN RANGE 1-8 \n'):
                        sys.stdout.write(character)
                        time.sleep(0.003)

                elif number_that_player_wants_to_move in lst_of_numbers_that_can_be_moved: #check if player's move is valid
                    index_number = original_state.index(number_that_player_wants_to_move) #index position of number that player wants to move
                    index_empty_spot = original_state.index(' ') # index position of empty spot
                    to_be_replaced = original_state[index_empty_spot] # changing position of number to empty spot
                    original_state[index_empty_spot] = number_that_player_wants_to_move # change spot of empty string to from input - "to_move"
                    original_state[index_number] = ' ' #change previous spot of number in "to_move" to ' ' empty string.
                    break
                else:
                    for character in (f"SORRY, YOU CANNOT ENTER '{number_that_player_wants_to_move}' AS IT IS NOT NEXT TO THE EMPTY BLANK; PLEASE ENTER A NUMBER NEXT TO THE BLANK \n"):
                        sys.stdout.write(character)
                        time.sleep(0.003)
        else:
            pass

        print('\n')


        print(' ',original_state[0],' ','|',' ',original_state[1],' ','|',' ',original_state[2],' ',sep = '') #PRINT THE  FIRST ROW OF THE MATRIX 
        print ('---|---|---')
        print(' ',original_state[3],' ','|',' ',original_state[4],' ','|',' ',original_state[5],' ',sep = '') #PRINT THE SECOND ROW OF THE MATRIX
        print ('---|---|---')
        print(' ',original_state[6],' ','|',' ',original_state[7],' ','|',' ',original_state[8],' ',sep = '') #PRINT THE  THIRD ROW OF THE MATRIX

        count_of_loops += 1

    

    if original_state[0:8] == sorted(original_state)[1:9]: #check if the player has successfully sorted the list
        print((lst_of_praises[random.randint(0,6)]).upper())
        quit()
    else:
        pass

def play_Tiles(choice):
    if 'tiles' in choice or 'y' in choice:
        while 'tiles' in choice or 'y' in choice:
            #Define variables:
            original_state = []#empty list that will be used to append the empty spaces based on the difficulty level
            lst_of_numbers = [] #lst that will contain randomised numbers based on the player's choice of difficulty
            points =  0 #score of the player for every time he successfull completes the game
            empty_space = ' ' # empty space in the matrix so that player can move the numbers
            index = [] #var used to store the index positions of 
            numberCountIngame=0 # storing length of "original_state" (later on)
            index_location_of_emptyPosition = 0
            
            welcome_statement = ('\n\nWELCOME TO TILES, A GAME OF LOGIC AND PATIENCE. \nIN THIS GAME, YOU WILL BE GIVEN A 3x3 SCRAMBLED MATRIX. \nTHE EMPTY CELL IS WHERE YOU CAN MAKE YOUR MOVE. \nYOU HAVE TO SORT IT IN ASCENDING ORDER (1 ON THE TOP LEFT CORNER, AND THE EMPTY SQUARE ON THE BOTTOM RIGHT CORNER). \nANYTIME YOU WANT TO QUIT, JUST ENTER "QUIT". \nBEST OF LUCK  ')
            for character in welcome_statement:
                sys.stdout.write(character)
                time.sleep(0.03)
            #retreiving the size of matrix
            #list_of_difficulty_words = ['1','easy','2','medium','3','hard']            
            #difficulty_level = (input('What level of difficulty do you want to play (1-EASY / 2-MEDIUM / 3-HARD): ')).lower() #ask for input based on user's choice of difficulty
            #while difficulty_level not in list_of_difficulty_words:
             #   difficulty_level = input(f"Sorry, but you cannot enter '{difficulty_level}'. You can only enter (1-EASY / 2-MEDIUM / 3-HARD) ") #prompting player to enter correct keywords
                      
            original_state=len_and_shuffling_of_matrix(original_state) 

            
            #print(original_state)
            
            #printing the matrix
            
            printing_randomisedMatrix(original_state)

                                   
            choice = (input('DO YOU WANT TO CONTINUE(Y/N): ')).lower()
            if choice == 'n':
                print('THANKS')
                break
#to run this program as a main program
if __name__ == '__main__': 
    choice = (input('WHAT GAME DO YOU WANT TO PLAY: ')).lower()
    play_Tiles(choice)
