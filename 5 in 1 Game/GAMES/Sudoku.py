import sys
import time
import random
def sudoku_matrix_generator(rows):
    """
    This function generate the matrix for the suduko game
    It generate first row with 9 number (between 1-9) in random sequence
    Using first row, it generate the second row by shifing 3 positions 
    Using second row it generate the third row by shifing 3 positions
    Using thrrd row it generate the fourth row by shifing 1 position
    Using fourth row, it generate the fifth row by shifing 3 positions
    Using fifth row it generate the sixth row by shifing 3 positions
    Using sixth row it generate the seventh row by shifing 1 position
    Using seventh row, it generate the eighth row by shifing 3 positions
    Using eighth row it generate the nineth row by shifing 3 positions
    poistion shifting rule row wise
    [0,3,3,1,3,3,1,3,3]

    parameter
    ---------
    rows: int
        number of rows in suduko game
    Returns
    -------
    dictionary: dict
        storing the matrix in key value pair form (i.e number and its index location)
    """

    rows =int(rows) 
    get9RandomDigitsList = random.sample(range(1,rows+1),rows) #randomise the order of 9 numbers (from 1-9), such that there are no duplicates and append it to the list
    #[8, 5, 3, 6, 7, 1, 9, 2, 4]
    rules =[0,3,3,1,3,3,1,3,3] #index position shifting rule
    index=0 
    rulesCounter=0 
    dictionary={} #because it contains key-val pair, where key is the index lacation of the number and the val is the number
    dictionary_key=0
    #mainList=[]
    #sett
    for i in range(0,len(rules)):
        rulesCounter +=rules[i] #moving index position of numbers for subsequrnt rows
        for j in range(0,len(rules)): #setting the row of numbers (row1-row9)
            index = j+rulesCounter 
            if index > 8:
                index = index%9
                #print(index)
            dictionary[dictionary_key]=get9RandomDigitsList[index]
            #sublist.append(get9RandomDigitsList[index])
            dictionary_key += 1
        #mainList.append(sublist)
    return dictionary
            


"""
"""

def print_sudoku_table(dictionary):

    """
    This function randomly blanks the values of the dictionary. it stores ALL the keys into a list and prints out the list
    
    parameters
    ----------
    dictionary: dict
        it is the dictionary that contains the randomly generated values    

    """
    rows = cols = int(len(dictionary)**0.5) #set len of row and col to 9
    for i in range (0,rows):
        i+=1
    counter1=0
    main_matrix = []
    for x in range(rows):
        sub_matrix = []
        for y in range(cols):
            sub_matrix.append(dictionary.get(counter1)) 
            counter1+=1
        main_matrix.append(sub_matrix)
    for i in range(rows):
        print(f'....'*cols) #printing the dotted line at the top of every row
        for j in range(cols):
            if j == cols-1:
                print(f"| {main_matrix[i][j]} | ",end = '')
            else:
                print(f"| {main_matrix[i][j]} ",end = '')
        print(f"\n",end = '')
    print(f'....'*cols) #printing line at the end of the last row to complete the box


def sudoku_matrix_final (dictionary):
    
    import copy
    
    dictionary_with_hidden_values = copy.deepcopy(dictionary) #copy 
    y = 0
    num_of_rows = (int(len(dictionary_with_hidden_values)**0.5))
    indexes_to_be_blanked = []
    for i in range(0,num_of_rows):
       # number_of_blanks = random.randint(3,num_of_rows-2)
        number_of_blanks = random.randint(3,8) #generating the number of blanks

        indexes_to_be_blanked = random.sample(range(y,y+num_of_rows),number_of_blanks) #blank indexes 
        for j in range (number_of_blanks):
            dictionary_with_hidden_values[indexes_to_be_blanked[j]] = ' '
        y+=num_of_rows
    return dictionary_with_hidden_values



            
def play_sudoku (choice): 

    """
    this function asks the user for input, and checks its validity. Based on that, it fills up that cell location

    parameters
    ----------
    choice: str
        this is the choice of game the player wants to play

    """
    lst_of_praises = ['Well done!','Good job!','Bingo!', 'Great work!','Excellent!','Splendid!'] #praises that will be auto-generated if a player wins
    while ('sudoku' in choice) or 'y' in choice:
        welcome_text = ("WELCOME INTO SUDUKO! LET ME FAMILIARIZE YOU WITH THIS GAME: \nAT ANY TIME IN THE GAME, SHOULD YOU FEEL THAT YOU HAVE WRONGLY FILLED IN THE BOXES, ENTER `RESET`, AND IT WILL CLEAR ALL THE BOXES FOR YOU. \nHOWEVER, PLEASE NOTE THAT YOUR INPUTS ARE REPLACEABLE. \nTO QUIT, JUST ENTER `QUIT`, AND YOU WILL EXIT FROM THE GAME \n\n")
        for characters in welcome_text:
            sys.stdout.write(characters)
            time.sleep(0.01)
        #Defining variables:
        dictionary_of_indexes_and_numbers_that_have_been_said = {} #Empty dictionary to store the move made, and its index location
        players_box_to_fill_number = ''
        #Calling matrix from sub-functions:
        dictionary=sudoku_matrix_generator(9) # preparing and safekeeping the matrix for checking
        dictionary_with_hidden_values = sudoku_matrix_final(dictionary)
        for i in range(len(dictionary_with_hidden_values)):
            if ' ' in str(dictionary_with_hidden_values[i]): 
                dictionary_of_indexes_and_numbers_that_have_been_said[i+1] = ' '
            else:
                pass

        print_sudoku_table(dictionary_with_hidden_values)
        len_dictionary = int(len(dictionary)) 
        size_of_column = int((len_dictionary)**0.5) #square root of the toatal no. of boxes in the matrix

        #Checking if matrix is correctly solved:
        while dictionary_with_hidden_values != dictionary: #keep on asking for input until he has correctly solved the sudoku game
            #Ask what box to enter number
            while True:
                players_box_to_fill_number = (input(f'WHICH BOX(1 - {len_dictionary}) DO YOU WANT TO ENTER YOUR NUMBER IN: ')).lower()
                #reset the game by clearing all player's filled cells
                if 'reset' in players_box_to_fill_number: 
                    for keys in dictionary_of_indexes_and_numbers_that_have_been_said:
                        dictionary_with_hidden_values[keys-1] = ' '
                        dictionary_of_indexes_and_numbers_that_have_been_said[keys] = ' '
                    break    
                elif 'quit' in players_box_to_fill_number:
                    quit_text = '*******************QUITTING FROM SUDOKU*******************. \n********************PLEASE TRY OUR OTHER GAMES. HAVE A NICE DAY*******************.'
                    for character in quit_text:
                        sys.stdout.write(character)
                        time.sleep(0.03)
                    sys.exit()


                

                #check if input is a number, and it is in the key of "dictionary" , and check if the input has not been prviously entered by the programme
                elif (players_box_to_fill_number.isnumeric()) and (int(players_box_to_fill_number) in range(1,len_dictionary+1)) and (int(players_box_to_fill_number) in dictionary_of_indexes_and_numbers_that_have_been_said.keys()): 

                    players_box_to_fill_number = int(players_box_to_fill_number)
                    break

                else:
                    if (players_box_to_fill_number) not in range (1,82):
                        print(f'SORRY, YOU CANNOT ENTER "{players_box_to_fill_number}"; YOU CAN ONLY ENTER NUMBERS FOR BOXES IN RANGE FROM 1 - {len_dictionary}')
                    else:
                        print(f'SORRY, YOU CANNOT ENTER "{players_box_to_fill_number}"; AS THE PROGRAM HAS ALREADY GENERATED A NUMBER IN THAT BOX.')
                #troubleshoot
                #print (dictionary_with_hidden_values[int(players_box_to_fill_number)-1])#printing box number of player's choice

            if 'reset' in str(players_box_to_fill_number): #check if player wants to clear all the squares
                reset_text = '\n\n*******************RESETTING THE MATRIX******************* \n*******************CLEARING ALL INPUTS******************\n\n'
                for characters in reset_text:
                    sys.stdout.write(characters)
                    time.sleep(0.05)
                

                print_sudoku_table(dictionary_with_hidden_values)
                pass
            else:

                #Ask what number player wants to move
                while True: #keep on asking player to enter a valid input
                    players_choice_of_number = input(f'WHICH NUMBER (1-{size_of_column}) DO YOU WANT TO ENTER IN BOX NUMBER {players_box_to_fill_number}: ') 

                    if players_choice_of_number.isnumeric() and int(players_choice_of_number) in range(1,size_of_column+1): #check if number is in range of 1-9
                        break
                    else:
                        print(f'SORRY, YOU CANNOT ENTER "{players_choice_of_number}"; THE NUMBER YOU HAVE ENTERED IS NOT A NUMBER IN RANGE FROM 1-9.')


                #print("\n\ndictionary_of_indexes_and_numbers_that_have_been_said:",dictionary_of_indexes_and_numbers_that_have_been_said)

                #check if he is entering an empty box or has he previously filled it:
                if ((players_box_to_fill_number) in dictionary_of_indexes_and_numbers_that_have_been_said.keys()) and (str((dictionary_of_indexes_and_numbers_that_have_been_said[players_box_to_fill_number])).isnumeric()):
                    replace_or_not_replace = (input(f'ARE YOU SURE THAT YOU WANT TO REPLACE THE NUMBER IN BOX {players_box_to_fill_number}: ')).lower() #check if player wants to replace previously-entered box
                    if 'y' in replace_or_not_replace:
                        dictionary_with_hidden_values[int(players_box_to_fill_number)-1] = int(players_choice_of_number) #add the 

                        #updating matrix with players choice of number and storing it in "dictionary_of_numbers_and_indexes_that_have_been_said"
                        dictionary_of_indexes_and_numbers_that_have_been_said[players_box_to_fill_number] = int(players_choice_of_number)
                        print_sudoku_table(dictionary_with_hidden_values)
                else:
                    dictionary_with_hidden_values[int(players_box_to_fill_number)-1] = int(players_choice_of_number)
                    dictionary_of_indexes_and_numbers_that_have_been_said[players_box_to_fill_number] = int(players_choice_of_number)

                    print_sudoku_table(dictionary_with_hidden_values)
                    #troubleshoot
                    #print(dictionary_of_indexes_and_numbers_that_have_been_said)


        #If player wants to quit
        if 'y' in str(players_box_to_fill_number):
            pass
            # #print('''Quitting from Sudoku.Please try our other games.   Have a nice day.''')
        else:
            if dictionary_with_hidden_values == dictionary:
                for characters in (f'{(lst_of_praises[random.randint(0,6)]).upper()}, YOU HAVE CORRECTLY SOLVED THE SUDOKU PUZZEL! \n'):
                    sys.stdout.write(characters)
                    time.sleep(0.05)
                choice = (input('DO YOU WANT TO PLAY AGAIN: ')).lower()
                if 'n' in choice:
                    break
                else:
                    pass
#to run this program as a main program
if __name__  == '__main__':        
    choice = (input('WHAT GAME DO YOU WANT TO PLAY (ENTER SUDOKU): ')).lower()
    play_sudoku(choice)
