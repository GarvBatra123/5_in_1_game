#var = variable
#no. of correct digits
#no. of digits in correct position

#choice = (input('What game do you want to play: ')).lower()
import time
import sys
import random #to generate x-digit number randomly
def mastermind(choice):
    """
    In this function, a random number is generated and replaced by underscores. The player has to guess the number within a given number of tries

    Parameters
    ----------
    choice: Str
        this is the choice of game the player has entered


    """

    choice1=''
    if ('master' in choice and 'mind' in choice):
        count_of_number_of_games_played = 0
        while ('master' in choice and 'mind' in choice) or 'y' in choice1:
            
            #Defining variables:
            output_of_underscores = [] # var used to store '_' instead of the numbers.
            lst_of_numbers_that_have_been_said = [] # used to store all the numbers that have already been guessed (to prevent the person from guessing that number again)
            original_number_breakdown =[] # used to store individual characters from original number.
            entered_number_breakdown = [] # used to store individual characters from guessed number
            index = 0 # var used to go through every digit in "entered_number_breakdown" and "number"
            right_position = 0 #var used to store how many numbers are placed correctly
            #>>>wrong_position = 0 #var used to store how many numbers are placed wronly
            number_present = 0 #var used to store how many numbers are present in the actual number and guessed number
            #>>>number_not_present = 0 #var used to store how many numbers are not present in the actual number but in the guessed number
            lst_of_praises = ['Well done!','Good job!','Bingo!', 'Great work!','Excellent!','Splendid!'] #praises that will be auto-generated if a player guesses the number correctly
            number_of_tries = 11 #var used to store the number of tries player has left (11-1) and so on, as the player only gets a maximum of 11 tries before losing
            points = 0 #var used to store the total points the player has gotten
            lst_of_difficulty_words = ['easy','medium','hard']
                        
            if count_of_number_of_games_played == 0:
            #Printing instructions
                welcome_text = ("WELCOME TO MASTERMIND: CODEMAKER VS CODEBREAKER. THIS IS A GAME OF LOGIC, DEDUCTION AND SMART THINKING. BEFORE YOU PLAY, I MUST FAMILIARIZE YOU WITH THE RULES OF THIS GAME: \n\n1.A NUMBER WILL BE GENRATED BASED ON YOUR PREFERNCE OF DIFFICULTY LEVEL : EASY , MEDIUM, HARD  \n\t 'EASY' - 3-DIGIT NUMBER \n\t 'MEDIUM' - 4-DIGIT NUMBER \n\t 'HARD' - 5-DIGIT NUMBER \n\n2.YOU WILL BE THE CODEBREAKER, WHILE THE CPU WILL BE THE CODEMAKER \n\n3.YOU WILL BE GIVEN 11 TRIES TO GUESS THE CORRECT NUMBER. CLUES WILL BE GIVEN AS YOU KEY IN YOUR NUMBER. \nIF YOU WANT TO QUIT, JUST ENTER 'QUIT'. \nBEST OF LUCK \n\n")
                for character in welcome_text:
                    sys.stdout.write(character)
                    time.sleep(0.01)


                        
            #Generating random number:           
            difficulty_level = (input('\nPLEASE ENTER WHAT LEVEL OF DIFFICULTY DO YOU WANT TO PLAY (EASY / MEDIUM / HARD): ')).lower()
            
            
            while difficulty_level not in lst_of_difficulty_words:
                difficulty_level = (input(f"\nYOU CANNOT ENTER '{difficulty_level}' PLEASE ENTER WHAT LEVEL OF DIFFICULTY DO YOU WANT TO PLAY (YOU CAN ONLY ENTER 'EASY' OR 'MEDIUM' OR 'HARD'): ")).lower()            
            if difficulty_level == 'easy':
                number = random.randint(100,999) #var used to store the no. generated that will be used in the code
                #number = 100
            elif difficulty_level == 'medium':
                number = random.randint(1000,9999) #var used to store the no. generated that will be used in the code
                #number = 1000
            elif difficulty_level == 'hard':
                number = random.randint(10000,99999) #var used to store the no. generated that will be used in the code
                #number = 10000
                    
                
            #Replacing the number (generated above 👆) with dashes to be printed out
            for i in str(number):
                output_of_underscores.append('__') #print '__' instead of the actual no.
            print('\n',' '.join(output_of_underscores)) #print the dashes based on the number of characters in "number"
            #print(number)
            
            
            #Check if number inputted is correct or not, or how close is it to the actual number
            while number_of_tries > 0:
                while True:
                    enter_number = (input(f'\nPLEASE ENTER THE {len(str(number))}-DIGIT NUMBER THAT YOU HAVE GUESSED: '))
                    #check if number is shorter or longer than the randomized number :
                    #exit when player enter 'quit'
                    if ('quit' in enter_number):
                        choice1='n'
                        break

                    if enter_number.isnumeric() and len(str(int(enter_number))) == len(str(number)): #check whether player has not entered a string of alphabets, but has given a correct digit number,
                        break
                    else:
                        print(f'\nSORRY, YOU HAVE NOT ENTERED A {len(str(number))}-DIGIT NUMBER. PLEASE ENTER {len(str(number))}-DIGIT A NUMBER: ')

                #enter_number = int(enter_number)            
                while (str(enter_number) != str(number) and 'n' not in choice1) :
                    
                    entered_number_breakdown = []
                    original_number_breakdown = []
                    index = 0 #reset value of index after every while loop
                    right_position = 0 #reset value of "right_position" after every while loop
                    number_present = 0 #reset value of "wrong_position" after every while loop
                    for i in range(len(str(number))):
                        original_number_breakdown.append(str(number)[i])
                    #print("original_number_breakdown:",original_number_breakdown)
                    for i in range(len(str(enter_number))):
                        entered_number_breakdown.append(str(enter_number)[i]) #break down guessed no.into
                    #print("entered_number_breakdown:",entered_number_breakdown)
                                           
                    for i in (str(number)): #convert number to string to compare each index of the guessed word and the original word
                        #checking if indexes of entered number are placed in correct positions
                        if entered_number_breakdown[index] == (str(number))[index]: # is the index location of the entered word == to that index location of the actual number?
                            right_position += 1 #increase right position by 1 
                            #print("right_position:",True)
                        else:
                            pass   
                        if entered_number_breakdown[index] in original_number_breakdown: #count no. of right digits in the guessed no.
                            number_present +=1
                            #print("number_present:",True)  
                        else:
                            pass
                        index += 1  #increase index by 1 to check if the next digit fulfills the criteria above or not
                    #print("right_position:",right_position)
                    #print("number_present:",number_present)
                    
                    #append the numbers that have been said to this list, to prevent player from re-entering the same number again
                    lst_of_numbers_that_have_been_said.append(f"{enter_number} -  CORRECT POSITION : {right_position}          CORRECT DIGITS: {number_present} ") 
                    print('\n')
                    print('\n'.join(lst_of_numbers_that_have_been_said)) # print list of numbers that have been said with clues.
                    number_of_tries -= 1


                    if number_of_tries == 0: #check if player has run out of tries
                        print(f"\n\nTHE NUMBER WAS : {number}")
                        while True:
                            choice1 = (input(f"\nSORRY, BUT YOU HAVE USED UP ALL YOUR TRIES. WOULD YOU LIKE TO PLAY AGAIN (Y/N): ")).lower()
                            if ('n' in choice1 or 'quit' in choice1 or 'y' in choice1):
                                break

                        if 'n' in choice1 or 'quit' in choice1:  #if player doesnt want to play again                                                  
                            choice1='n'
                            break
                        elif 'y' in choice1:  #if player wants to play again
                            count_of_number_of_games_played += 1

                            #print('choice1 = y')
                            break
                            
                    else:    
                        print(f'\nYOU NOW HAVE {number_of_tries} TRIES LEFT.')#display no. of tries left
                        #enter_number = (input('\nPlease enter the number that you have guessed: '))
             
                        break
             

                if str(enter_number) == str(number): #check if the input the player has entered is correct?
                    number_of_tries = 0
                    print(lst_of_praises[random.randint(0,len(lst_of_praises)-1)],'YOU HAVE CRACKED THE NUMBER!') #Print the praises if player gets it correct
                    while True:
                        choice1 = (input('\nDO YOU WANT TO PLAY AGAIN (Y/N): ')).lower()
                        if ('n' in choice1 or 'quit' in choice1 or 'y' in choice1):
                            break
                if 'n' in choice1 or 'quit' in choice1:
                    choice1='n' 
                    break
            
            if 'n' in choice1:
                for characters in ('*******************QUITTING FROM MASTERMIND******************** \nTHANK YOU FOR PLAYING MASTERMIND. HOPE YOU HAD FUN 😜!'):
                    sys.stdout.write(characters)
                    time.sleep(0.01)

                print('')
                sys.exit()
#to run this program as a main program
if __name__ == '__main__':
    choice = (input('WHAT GAME DO YOU WANT TO PLAY: ')).lower()    
    mastermind(choice)
