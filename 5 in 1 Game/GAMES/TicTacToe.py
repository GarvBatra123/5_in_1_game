import random
import sys
def player_1_win_check (original_state,end_of_round_check,score,player_symbol): 

    """
        This function is used to iterate through each index of the list and check whether the player has entered an 'X' or 'O' in the following combination of indexes:
            [0,1,2] OR [3,4,5] OR [6,7,8] OR  [0,3,6] OR [1,4,7] 0R [2,5,8] OR [0,4,8] OR [2,4,6]
        If the player has fulfilled any one of the conditions, the score will be incremented by 1 
       
        Parameters:
        ------------
        original_state: List
            this is a list of string that contains the moves played by the player. 
        end_of_round_check: Boolean 
            this is to set whether this is the end of the current round
        score: integer
            incrementing the score of the player
        player_symbol: Str 
            passed as either 'X' or 'O' based on player
   
        Returns
        --------
        Array
            contains the check to end this round or continue, and player's score

    """  
       
    if (player_symbol in  original_state[0] and player_symbol in  original_state[1] and player_symbol in original_state[2]) \
    or (player_symbol in  original_state[3] and player_symbol in  original_state[4] and player_symbol in original_state[5]) \
    or (player_symbol in  original_state[6] and player_symbol in  original_state[7] and player_symbol in original_state[8]) \
    or (player_symbol in  original_state[0] and player_symbol in  original_state[3] and player_symbol in original_state[6]) \
    or (player_symbol in  original_state[1] and player_symbol in  original_state[4] and player_symbol in original_state[7]) \
    or (player_symbol in  original_state[2] and player_symbol in  original_state[5] and player_symbol in original_state[8]) \
    or (player_symbol in original_state [0] and player_symbol in  original_state[4] and player_symbol in original_state[8]) \
    or (player_symbol in  original_state[2] and player_symbol in  original_state[4] and player_symbol in original_state[6]): 
        end_of_round_check = True #Set to True if player has met the condition   
        score += 1 #increase points of the player
    else:
        end_of_round_check = False #if player doesnt align any of his 'x' correctly, he should not get a point

    return end_of_round_check, score

def printing_matrix(original_state): 
    """ This function is printing the 3x3 matrix after the user has keyed-in their input
        Parameters
        ----------
        original_state: List
            this is a list of string that contains the moves played by the player. 
    """
    print('\n')
    print(original_state[0],'|',original_state[1],'|',original_state[2],sep = '') #PRINT THE  FIRST ROW OF THE MATRIX 
    print ('---|---|---')
    print(original_state[3],'|',original_state[4],'|',original_state[5],sep = '') #PRINT THE SECOND ROW OF THE MATRIX
    print ('---|---|---')
    print(original_state[6],'|',original_state[7],'|',original_state[8],sep = '') #PRINT THE  THIRD ROW OF THE MATRIX

def display_player_score (score1,player1,player2,score2,has_player1_won_the_round,has_player2_won_the_round):  
    """
        This function will print the scores of each player 
        
        Parameters
        ----------
        socre1: int
            score of player1
        player1: str
            name of player1
        socre2: int
            score of player2
        player2: str
            name of player2

    """
    if has_player1_won_the_round == True:
        print(f'\nCONGRATULATIONS {player1}! YOU HAVE WON THE ROUND!')
    elif has_player2_won_the_round == True:
        print(f'\nCONGRATULATIONS {player2}! YOU HAVE WON THIS ROUND!')
    if score1+score2 < 3: #keep on repeating 3 times
        print(f'{player1} HAS {score1} POINT(S)! \n{player2} HAS {score2} POINT(S)! \nROUND ENDED ---- NEW ROUND STARTING:') #if player1 wins a round, display the total points each player has 
    else:
        pass
    
def play_tictactoe(choice): #define game
    """
        1.This is the main function.
        2.It asks both players for their names respectively
        3.It validates whether both names are duplicate, or the name is empty 
        4.It asks each player respectively for input where they wants to make their respective move 
        5.Based on the chosen move above from (4), it fills up the cell for each player
        6.It checks whether that cell is blank or it is already filled
        7.If a player wins, he gets a point and a new round starts
        8.It repeats steps 4-8 until the total score of both player is equal to 3

        Parameters
        ----------
        choice: string
            Choice of game passed from "MYGAMEAPPLICATION.py"


    """
    player1_symbol=' X ' #player1 is always assigned to symbol 'X'
    player2_symbol=' O ' #player2 is always assigned to symbol 'O'
    if (("tic" in choice) and ("tac" in choice) and ("toe" in choice)) or ('y' in choice) or ('r' in choice): #check if player wants to quit
        while (("tic" in choice) and ("tac" in choice) and ("toe" in choice)) or ('y' in choice) or ('r' in choice): #keep on repeating while player wants to play
            #printing rules:
            print('WELCOME TO TIC TAC TOE: SINCE THIS IS A TEXT-BASED-GAME, LET ME FAMILIARIZE YOU WITH THE RULES: \n\n\n\tTHERE WILL BE MINIMUM OF 3 ROUNDS, AND THE PERSON WITH THE MOST POINTS AT THE END OF THESE 3 ROUNDS WILL WIN THE GAME. \n\n\tYOU WILL BE PRESENTED WITH A 3X3 MATRIX.\n\n\tAfter entering your names, you will have to enter what cell you want to place your "X" / "O" in.\n\n\tYou can only enter a 1-digit number from 1-9 ONLY. \n\n\tAnytime in the game, if you want to quit or restart, just enter "q" or "r" respectively. \n\n\tPlease note that player 1 will start 1st and has symbol "X", while player 2 will start 2nd and has symbol "O"')                                         
            
            while True: #keep on prompting both players to enter unique names
                player1 = (input('\n\n\nPlayer1-please enter your name: ')).strip() #ask player1 for name, & trim leading and trailing whitespaces 
                if player1 == '':
                    print('Name cannot be empty. Please re-enter player1 name')  
                else:                
                    while True:
                        player2 = (input('Player2-please enter your name: ')).strip() #Ask player2 for name
                        if player2 =='':
                            print('Name cannot be empty. Please re-enter player2 name') 
                        else:
                            break

                    if (player2).lower() == (player1).lower(): #check if names are duplicates
                        print('Both of you have entered duplicate names. Please re-enter 2 DIFFERENT names: ') 
                    else:
                        break
                
                
            player_1_score = 0 #setting score of player1 at start of game to 0
            player_2_score = 0 #setting score of player2 at start of game to 0

            ##Indicators to check which player has won the round
            has_player1_won_the_round = False # setting "has player1 won" to false at the start of game 
            has_player2_won_the_round = False # setting "has player2 won" to false at the start of game 

            while (player_1_score + player_2_score) < 3: #keep on repeating the game for 3 rounds
                counter = 0 #variable used to store number of moves played
                original_state = [' 1 ',' 2 ',' 3 ',               #9 char list to be printed out as a 3x3 matrix
                                  ' 4 ',' 5 ',' 6 ',
                                  ' 7 ',' 8 ',' 9 ']
               
                printing_matrix(original_state) #print the 3x3 matrix
                
                while counter < 9: #keep on repeating while there are moves left

                    #PLAYER_1
                    while True:
                        position_player1 = ((input(f'\nHi {player1}! what cell do you want to place an "X" in(1-9 ONLY): '))).lower() # variable to store player1's move 
                        choice = ''
                        #Restart
                        if 'r' in position_player1: #check if player1 wants to restart
                            position_player2 = (input(f"Hi {player2}, are you ok to restart this game.This will restart the whole game, and you will lose all your points. (y/n): ")).lower() #ask player2 if he is ok to restart as well
                            if 'y' in position_player2: #if player2 agrees: 
                                choice = 'restart' #set choice to restart to break out of this game 
                                break  
                            else:
                                print(f'Sorry {player1}, but {player2} wants to continue. You cannot restart. You have to play on.') #do not restart if player2 doesnt agree
                        #quitting
                        elif 'q' in position_player1: #check if player1 wants to quit
                            position_player2 = (input(f"Hi {player2}, are you ok to quit from this game. (y/n): ")).lower()#ask player2 if he is willing to quit
                            if 'y' in position_player2: #if both agree, assign choice = 'quit' and break out of the game, and leave
                                print("\n                  ***************QUITTING FROM TIC TAC TOE***************\n***************THANK YOU FOR PLAYING WITH US. PLEASE TRY OUT OUR OTHER GAMES***************")
                                sys.exit()
                            else:
                                print(f'Sorry {player1}, but {player2} wants to continue. You cannot quit. You have to play on.') #do not quit if player2 doesnt agree
                            
                        
                        else:
                            if ((position_player1).isnumeric() == False) or (len(position_player1) > 1): #if "position_player1" is not numeric, ask him to input again
                                print(f'Sorry, "{position_player1}" is not allowed. You can only enter numbers from 1-9')
                            elif 'O' in original_state[int(position_player1)-1]: #check if implayer2 has already placed an 'o' in that position
                                print(f"Sorry, you can't enter {position_player1} as {player2} has already placed an 'O' over there.")
                            elif 'X' in original_state[int(position_player1)-1]: #check if player1 has already placed an 'x' in that position
                                print(f"Sorry, but you cannot replace cell {position_player1} with 'X', as you have previously placed an 'X' over there")
                            
                            else: #else, let player1 enter 'x' in that position
                                position_player1 = int(position_player1) #convert position_player1 into an int type
                                original_state[position_player1-1] = player1_symbol
                                break
                    #storing return values in array
                    arr = player_1_win_check (original_state,has_player1_won_the_round,player_1_score,player1_symbol)
                    has_player1_won_the_round = arr[0] #return the "has_player1_won_the_round" check
                    player_1_score =arr[1] #return the score of the player1
                    
                    printing_matrix(original_state) #printing the newly-assigned matrix
                    if has_player1_won_the_round == True:
                        display_player_score (player_1_score,player1,player2,player_2_score,has_player1_won_the_round,has_player2_won_the_round) #print the total score of each player after player1 wins one point
                        break  
                    else:
                        pass

                    if choice == 'restart': #restart the game
                        print('***************RESTARTING TIC TAC TOE***************')
                        break   
                   
                    
                    counter+=1 #increase counter by 1 to check if the matrix is fully occupied
                    if counter == 9: #check if matrix is fully occupied
                        break
                    
                    #PLAYER_2
                    else:
                        #to restart the FULL game
                        if choice == 'restart':
                            pass
                        else:
                            while True:
                                position_player2 = ((input(f'\nHi {player2}! what cell do you want to place an "O" in (1-9 ONLY): '))).lower() #ask player2 what position he wants to move to
                                if 'r' in position_player2: #check if player2 wants to restart
                                    position_player1 = (input(f"Hi {player1}, are you ok to restart this game.This will restart the whole game, and you will lose all your points. (y/n): ")).lower() #ask player1 if he is ok to restart
                                    if 'y' in position_player1: #if player1 agrees, restart
                                        choice = 'restart'
                                        break  

                                    else:
                                        print(f'Sorry {player2}, but {player1} wants to continue. You cannot restart. You have to play on.') #if player1 doesnt agree, do not restart
                                #quit from game
                                elif 'q' in position_player2: #check if player2 wants to quit
                                    position_player1 = (input(f"Hi {player1}, are you ok to quit from this game. (y/n): ")).lower() #ask player1 if he is ok to quit
                                    if 'y' in position_player1: #if player1 agrees, break and quit from game
                                        print("\n                  ***************QUITTING FROM TIC TAC TOE***************\n***************THANK YOU FOR PLAYING WITH US. PLEASE TRY OUT OUR OTHER GAMES***************")
                                        sys.exit()

                                        
                                    else:
                                        print(f'Sorry {player2}, but {player1} wants to continue.You cannot quit. You have to play on.') #if player1 doesnt agree, do not quit



                                else:
                                    if ((position_player2).isnumeric() == False) or (len(position_player2) > 1): #check if position_player2 is numeric or not
                                        print(f'Sorry, {position_player2} is not allowed. You can only enter numbers from 1-9')
                                    elif player1_symbol in original_state[int(position_player2)-1]: # check if 'X' is already in the position entered in position_player2
                                        print(f"Sorry, you can't enter {position_player2} as {player1} has already placed an 'X' over there.")
                                    elif player2_symbol in original_state[int(position_player2)-1]: # check if 'O' is already in the position entered in position_player2
                                        print(f"Sorry, but you cannot replace cell {position_player2} with 'O', as you have previously placed an 'O' over there")
                                    else:
                                        position_player2 = int(position_player2) 
                                        original_state[position_player2-1] = player2_symbol
                                        break
                        #storing return values in array
                        arr2 =  player_1_win_check (original_state,has_player2_won_the_round,player_2_score, player2_symbol)               
                        has_player2_won_the_round = arr2[0] #check if player2 has won a point by aligning properly or not and return has_player2_won_the_round
                        player_2_score =arr2[1] #return player2 score
                        #print((player_2_win_check(original_state,has_player2_won_the_round,player_2_score,player_1_score)))
                        #print('player_2_score:',player_2_score)
                        if choice == 'restart': #if both players want to restart
                            print('\n***************RESTARTING TIC TAC TOE***************\n')
                            break                      
                        else:
                            pass
                        printing_matrix(original_state)
                        if has_player2_won_the_round == True: #check if player2 has won the round
                            display_player_score (player_1_score,player1,player2,player_2_score,has_player1_won_the_round,has_player2_won_the_round) 
                            break
                        counter+=1 #increment the number of moves played

                
                if choice == 'restart' : #check if players wanted to quit or restart
                    break
                elif has_player1_won_the_round == False and has_player2_won_the_round == False: #if no one has gotten a score, it is a tie
                    print('\n***************THIS IS A DRAW: NO ONE WINS A POINT*************** \n***************ROUND ENDED ---- NEW ROUND STARTING*************** ')

            if choice == 'restart':
                pass
            elif choice == 'quit':
                break
            else:
                if player_1_score > player_2_score: #congratulating player 1 for winning game if he has more points than player2
                    print(f'\n***************{player1.upper()} HAS WON THE GAME BY {player_1_score-player_2_score} POINT(S)! \nCONGRATULATIONS {player1.upper()}!***************')
                elif player_1_score == player_2_score: #if player_1_score == player_2_score
                    print(f'\n***************THE GAME HAS ENDED IN A DRAW! \nPLEASE TRY AGAIN LATER!***************')
                elif player_2_score > player_1_score: #congratulating player 2 for winning game if he has more points than player1
                    print(f'\n***************{player2.upper()} HAS WON THE GAME BY {player_2_score-player_1_score} POINT(S)!\nCONGRATULATIONS {player2.upper()}!***************')


                choice = input('do you want to play again (y/n): ') #ask if they want to play again
                if 'n' in choice:
                    break
                elif 'y' in choice:
                    pass
if __name__ == "__main__":
    # to be set from the MyGameApplication.py
    choice = (input('What game do you want to play: ')).lower() #ask user what game eh wants to play
    play_tictactoe(choice)
    
