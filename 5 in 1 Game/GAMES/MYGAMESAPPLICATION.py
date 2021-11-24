#import hangman1
#import mastermind1
#import tiles
#import sudobet
#######################

# open app and show display
#Show time and date on right hand corner:
from datetime import datetime #
#FFFFFF#ED2222
now = datetime.now()
#TIME:
current_time = now.strftime("%H:%M:%S %p")
time_now = ( current_time)

#DATE:

#Use time function to check for mng, noon, or evg (it is already defined so no need to do again):
hour = (str(time_now))

hour = (int(time_now[0:2]))
if 6 <= hour < 12:
    print(f'\n\n*****GOOD MORNING !****\n\n')
elif 12 <= hour <= 17:
    print(f'\n\n*****GOOD AFTERNOON !*****\n\n')
elif 17 < hour <= 23:
    print(f'\n\n*****GOOD EVENING !*****\n\n')
else:
    print(f'HELLO THERE !')

lst_of_games = ['Tic Tac Toe','Hang Man','Mastermind','Sudoku','Tiles']
print('THESE ARE THE GAMES AVAILABLE. PLEASE CHOOSE ONE OF THE FOLLOWING: ')
for i in range (0,len(lst_of_games)):
	print(lst_of_games[i], end = '\n')
	lst_of_games[i] = (lst_of_games[i]).lower()
    
#Ask what user wants to do?
while True:
	choice = ((input('\nPLEASE ENTER WHAT GAME YOU WANT TO PLAY: ')).strip()).lower() #choice is the user's selection of what he wants to do
	if choice not in lst_of_games:
		print(f'{choice.upper()} - YOU HAVE ENTERED AN INVALID NAME. PLEASE ENTER THE NAME FROM THE LIST SHOWN ABOVE. ')
	else:
		break
while choice in lst_of_games:
    if choice == 'tic tac toe':

            from TicTacToe import play_tictactoe
            play_tictactoe(choice)
            choice = (input('WHAT OTHER GAME DO YOU WANT TO PLAY: ')).lower()

    elif choice == 'hang man':
    	
            from Hangman import play_hangman
            play_hangman(choice)
            choice = (input('WHAT OTHER GAME DO YOU WANT TO PLAY: ')).lower()

    elif choice == 'mastermind':

            from Mastermind import mastermind
            mastermind(choice)
            choice = (input('WHAT OTHER GAME DO YOU WANT TO PLAY: ')).lower()

    elif choice == 'tiles':

            from Tiles import play_Tiles
            play_Tiles(choice)
            choice = (input('WHAT OTHER GAME DO YOU WANT TO PLAY: ')).lower()

    elif choice == 'sudoku':
            from Sudoku import play_sudoku
            play_sudoku(choice)
            choice = (input('WHAT OTHER GAME DO YOU WANT TO PLAY: ')).lower()







