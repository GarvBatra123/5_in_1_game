import random 
import time
import sys
def retrieving_word(topic):
    """  
    This function is used to randomly return a word from a list based on what topic the player wants.

    Paramaters
    ----------
    topic: str
        This is to store the topic the user wants to obtain the word from
    
    Ruturns
    -------
        Array
            randomly selected word based on the topic 

    """
    #LIST OF WORDS TO BE RETRIEVED BASED ON PLAYER'S CHOICE 
    list_of_words_birds = ['albatross','aviary','bald eagle','pelican','canary','chicken','goose','duck','hen','crow','dove','emu','falcon','flamingo','kingfisher','lark','owl','penguin','peacock']
    list_of_words_animals = ['alligator','anaconda','ant','ape','bear','baboon','beaver','bat','boar','blue whale','butterfly','cat','cheetah','camel','cobra','cow','crocodile','elephant','zebra']
    list_of_words_gemstones = ['aquamarine','amethyst','agate','alexandrite','amazonite','amber','beryl','bloodstone','calcite','citrine','diamond','fluorite','emrald','garnet','jasper','jade','lapiz lazuli','malachite','opal','onyx','pearl','peridot','pyrite','quartz','ruby','sapphire','topaz','tourmaline','turquoise','zircon']
    list_of_words_sports = ['archery','badminton','cricket','bowling','tennis','skateboarding','surfing','hockey','karate','yoga','volleyball','baseball','rugby','soccer','cycling','golf','football']
    lst_of_words_countries = ['afghanistan','albania','algeria','andaman and nicobar islands','bahamas','bhutan','beligum','bangladesh','brazil','canada','costa rica','cuba','denmark','equador','germany','greece','hungary','india','italy','kazakhstan','luxembourg','madascar','maldives','netherland','new zealand','north korea','parguay','portugal','romania','qatar','sweden','spain','united states of america','yemen','zimbabwe']

    if 'bird' in topic:
        count = random.randint(0,(len(list_of_words_birds)-1)) 
        full_word = list_of_words_birds[count]
        topic = 'BIRDS'
    elif 'animal' in topic:
        count = random.randint(0,(len(list_of_words_animals)-1))  
        full_word = list_of_words_animals[count]
        topic = 'ANIMALS'
    elif 'gemstone' in topic:
        count = random.randint(0,(len(list_of_words_gemstones)-1))     
        full_word = list_of_words_gemstones[count]    
        topic = 'GEMSTONES'
    elif 'sport' in topic:
        count = random.randint(0,(len(list_of_words_sports)-1))
        full_word = list_of_words_sports[count]  
        topic = 'SPORTS'
    elif 'countr' in topic:
        count = random.randint(0,(len(lst_of_words_countries)-1))
        full_word = lst_of_words_countries[count]  
        topic = 'COUNTRIES'
    return full_word



def generating_partially_blanked_word (full_word_list):
    """
    This function will generate the partially blanked word, with randomised alphabet(s) required for the user to enter the input
    
    input -> 'CROCODILE'
    output -> 'C _ _ _ _ _ _ L _', 4

    Parameters
    ----------
    full_word: str
        it contains the word that is to be blanked in this function
    
    Return
    -------
        lst_with_alph: list
        list of partially blanked alphabet(s)

        maximum_hint_count: int
            maximum hint count based on the length of the word

    """
    index=0
    lst_with_alph=[]
    #initialize the list with '_' and blank spaces ' '
    while index < len(full_word_list):
        if ' ' in full_word_list[index]: 
            lst_with_alph.append('  ') #replace sapce between 2 words with a '  ' (double spacebar)
        else:
            lst_with_alph.append('_') #replace alphabets with underscore ('_') 
        index += 1
    #set the randomize alphbets and max number of hints
    if len(full_word_list) <=4:
        count = random.sample(range(0,(len(full_word_list)-1)),1)[0] #randomly generate a number (index of alphabet in full_word) to be printed in the blank word i.e. _ _ c _ _ like this
        lst_with_alph[count] = full_word_list[count] #randomly generate ONE alphabet in the blanked word
        maximum_hint_count = 1 #maximum number of times the player can ask for hint

    elif 4 < len(full_word_list) <= 6:
        count = random.sample(range(0,(len(full_word_list)-1)),1)[0] #randomly generate a number (index of alphabet in full_word) to be printed in the blank word i.e. _ _ c _ _ like this
        lst_with_alph[count] = full_word_list[count] #randomly generate ONE alphabet in the blanked word
        maximum_hint_count = 2 #maximum number of times the player can ask for hint

    elif 10 > len(full_word_list) > 6:
        count = random.sample(range(0,(len(full_word_list)-1)),2) #randomly generate a number (index of alphabet in full_word) to be printed in the blank word i.e. _ _ c _ _ like this
        for i in range(2):
            lst_with_alph[count[i]] = full_word_list[count[i]]
        maximum_hint_count = 3 #maximum number of times the player can ask for hint
    else:
        count = random.sample(range(0,(len(full_word_list)-1)),3) #randomly generate a number (index of alphabet in full_word) to be printed in the blank word i.e. _ _ c _ _ like this
        for i in range(3):
            lst_with_alph[count[i]] = full_word_list[count[i]]
        maximum_hint_count = 4 #maximum number of times the player can ask for hint                      
    #return the list of partially blanked alphabet(s) and maximum hint count as array
    return lst_with_alph, maximum_hint_count

"""
this is driver function of this game
1. Get the randomized blanked word based on the selected topic
2. Prompt player to guess the alphabets or ask for hint until either the player gets the word correct or has exhuasted all the available tries/chance
"""
def play_hangman (choice):    
    count_of_number_of_games_played = 0 #count the number of games the player has played
    lst_of_praises = ['Well done!','Good job!','Bingo!', 'Great work!','Excellent!','Splendid!'] #praises that will be auto-generated if a player wins
    
    #if ('hang' in choice and 'man' in choice) or 'y' in choice:
    while ('hang' in choice and 'man' in choice) or 'y' in choice: #keep on repeating if user wants to (by inputting 'y' for yes at the end)
        #print(count_of_number_of_games_played)
        no_of_chances = 6 # variable used to store number of tries player has left if he enters wrong alphabet below
        lst_of_chr_that_have_been_said = [] #list used to stroe and print the letters that have been said to prevent deducting tries from player if he accidentally eneters same alphabet again
        lst_with_alph = [] # list used to store '_' and ' ' and alphabets (alph) that will be printed every time user enters an aplhabet
        index = 0 #index position of word that is retrieved from the specific topic list
        
        lst_of_empty_indexes = [] #if player asks for hint, you need to store the indexes in a list so that they can be replaced with the 

        #rules
        if count_of_number_of_games_played == 0: #print the rules only 1 time, in case the player wants to play again
            instructions = ['Welcome to Hangman! In this game, you will have to chose a topic from', '\t1.Birds', '\t2.Animals', '\t3.Gemstones', '\t4.Sports', '\t5.Countries', '\nBased on your choice of topic, a random word will be generated for you to guess', '\nYou will be given 6 chances to correctly guess the word.', '\nIf you guess an alphabet correctly, no chances will be deducted. Else, 1 chance will be deducted.', '\nYou will also be given hints, based on the length of the word. To ask for a hint, just enter "hint" Each hint will result in a deduction of 1 chance. \nSince this is a simple game, you will not be able to quit during a game.']
            for i in range(len(instructions)):
                print(instructions[i]) ; time.sleep (1.2)

        
        while True:
            topic = ((input('\n\nWHAT TOPIC DO YOU WANT TO GUESS?: ')).lower()).strip() # to help retrieve the word from the player's desired topic
            #print('\n',topic)
            if ('bird' in topic ) or ('animal' in topic ) or ('gemstone' in topic) or ('sport' in topic ) or ('countr' in topic):
                break
            else:
                print(f'SORRY, BUT "{topic.upper()}" IS AN INVALID KEYWORD. \nYOU CAN ONLY ENTER ONE THE FOLLOWING KEYWORDS: "ANIMALS", "BIRDS", "GEMSTONES", "SPORTS", OR "COUNTRIES"')

        #getting random word for the ent
        full_word = retrieving_word(topic)

        full_word_list = [y for y in list(full_word)] #each character in the input is stored in a list.    
        #storing return value of partially blanked word and maximum number of hints
        arr2 = generating_partially_blanked_word (full_word_list)
        lst_with_alph = arr2[0]
        maximum_hint_count = arr2[1]

        hint_count_variable = 0 #check the number of times the player has asked for hint

        output = ' '.join(lst_with_alph) #output of the blanked word
        #print('count_of_number_of_games_played',count_of_number_of_games_played)
        print(f'\n\nSINCE THE FOLLOWING WORD IS A {len(lst_with_alph)} ALPHABET WORD, YOU WILL ONLY GET { maximum_hint_count} HINT(S)')
        print(f'\n\nNUMBER OF HINTS: { maximum_hint_count - hint_count_variable} \nNUMBER OF TRIES: {no_of_chances}')
        print(output) #print the blanked word
        #print('l152:step1')
        #continue to play until as long as no_of_chances are more than 0 and alphabets to guess
        while no_of_chances != 0 and '_' in lst_with_alph :  #Keep on prompting player to enter input until he has 0 chances or/and and empty space('_') in the game                
            #print('num_count_in_game:',count_of_number_of_games_played)
            #print('number of chances:',no_of_chances)
            #print('l156: step2')
            
            while True:
                #print('l158:step3')
                #print(full_word)
                #print('TOPIC:',topic.upper()) #printing the topic
                alph = ((input('\nPLEASE ENTER ALPHABET: ')).lower()).strip() # ask for alphabet that the player wants to enter
                
                if 'hint' in alph : #check if player wants a hint
                    #print('l164:step4 (hint)')
                    lst_of_empty_indexes = [] #reasign 'lst_of_empty_indexes' to empty list to prevent it from re adding the indexes in the list
                    if hint_count_variable <  maximum_hint_count: #keep on letting the user ask for hints until he has run out of them
                        #print('l168:step5(hint)')
                        for i in range(len(lst_with_alph)):     #####
                            if '_' in lst_with_alph[i]:             ####  keep on finding empty indexes in the word to replace themwith alphabet
                                lst_of_empty_indexes.append(i)  #####     
                            
                        count = random.choice(lst_of_empty_indexes) #randomly choose any number (index) from the "lst_of_empty_indexes" and assign it to "count" so that the "_" in that index of the blanked word can te replaced with the alphabet in that index position of the original word
                        lst_with_alph[count] = full_word_list[count]#assiginng as from above ^^
                        hint_count_variable += 1 #count the number of times the player has asked for hints

                        #print(f'NUMBER OF HINTS: { maximum_hint_count - hint_count_variable} ')
                        no_of_chances -= 1 #deduct a chance from the player
                        #print(f'NUMBER OF TRIES: {no_of_chances}')
                        break #break from 'while True'
                    else:
                        print('SORRY, BUT YOU HAVE USED UP ALL OF YOUR HINTS. YOU CANNOT ASK FOR MORE HINTS')
                elif alph.isalpha() == False: #check if input is an alphabet or not
                    print(f"SORRY, BUT YOU CANNOT ENTER '{alph}' AS IT IS NOT AN ALPHABET. YOU CAN ONLY ENTER ALPHABETS / FULL WORD IF YOU KNOW WHAT THE WORD IS.")
                else:
                    break #break from 'while True'
            if alph == full_word: #check if the input = full word
                #print('l195:step7')
                print(lst_of_praises[random.randint(0,3)]) #praise the player if he wins
                choice = (input(f"DO YOU WANT TO PLAY AGAIN(Y/N)?: ")).lower() #ask if the player wants to play again
                break #break from outer while
            
            if alph not in lst_of_chr_that_have_been_said:
                #print('hint' not in alph)
                if alph in full_word_list:
                    #  print('l224:step11')
                    lst_of_chr_that_have_been_said.append(alph)
                     #append alphabets that have been said to prevent unnecessary deduction of chances if player accidently enters again the same alphabet again
                elif 'hint' not in alph: #if alphabet has not been said before and is not a 'hint' move
                    #print('l204:step9')
                    #print('l208:step10')
                    lst_of_chr_that_have_been_said.append(alph) #add the alphabet to the "lst_of_chr_that_have_been_said"
                    no_of_chances -= 1 #decrease the no. of chances player has remaining
                    #print('chances',no_of_chances)
                    if no_of_chances == 0: #check if player is out of chances
                        choice = (input(f"SORRY YOU HAVE FINISHED ALL YOUR CHANCES. \nTHE WORD WAS '{full_word}'. DO YOU WANT TO PLAY AGAIN(Y/N)?: ")).lower()
                        break #break from outer while
                    #else:
                        # print(f'NUMBER OF HINTS: { maximum_hint_count - hint_count_variable} ')
                        # print(f'NUMBER OF TRIES: {no_of_chances}')
            else: #lst_of_chr_that_have_been_said:
                print(f"\nYOU HAVE ALREADY ENTERED '{alph}', PLEASE ENTER ANOTHER ALPHABET.")


            
            while alph in full_word_list:
             #   print('l228:step12')
                place_value = full_word_list.index(alph) #get index of alph (input)
                lst_with_alph[place_value] = full_word_list[place_value] #replace blank in that index with alph
                full_word_list[place_value] = list(alph) 
            
            output = (' '.join(lst_with_alph))
            #print('l234:step13')
            
            print(f'\n\nNUMBER OF HINTS: { maximum_hint_count - hint_count_variable} \nNUMBER OF TRIES: {no_of_chances}')
            print(output)
            if len(lst_of_chr_that_have_been_said) > 0:
                print(f'\nWORDS / ALPHABETS THAT HAVE ALREADY BEEN ENTERED: {lst_of_chr_that_have_been_said}')

            #print('lst_with_alph:',''.join(lst_with_alph),',,,','full_word:',full_word)
            if (''.join(lst_with_alph)) == full_word:
                #print('l240:step14')
                print(lst_of_praises[random.randint(0,3)])
                choice = (input(f"DO YOU WANT TO PLAY AGAIN(Y/N)?: ")).lower()
                count_of_number_of_games_played += 1
                #print(count_of_number_of_games_played)
                #print(choice)
                break
        #print('l245:step15')
        #print(choice)
        if 'n' == choice:
            print('YOU ARE NOW EXITING HANGMAN! \nTHANK YOU FOR PLAYING HANGMAN. DO CHECK OUT OUR OTHER GAMES! ')

        elif 'y' == choice:
            #print('entering choice = y',count_of_number_of_games_played)

            count_of_number_of_games_played += 1
            #print(count_of_number_of_games_played)
            pass

if __name__ == '__main__':
    choice = (input('WHAT DO YOU WANT TO PLAY: ')).lower() #choice is users input of game he wants to play
    play_hangman(choice)
