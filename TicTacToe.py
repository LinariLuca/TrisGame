########################################################################################################################
# ATTENTION = This code is optimised for users running from the MacOS operating system.
# The reason is due to the fact that it is not possible to colour the boxes in one colour, but I have solved 
# this by highlighting their border with a different colour according to the winner, draw, loser situation.
# I enclose the forum link that explains 
# the problem ==> https://stackoverflow.com/questions/72056706/tkinter-button-background-color-is-not-working-in-mac-os
########################################################################################################################

import random 
from tkinter import * 
import numpy as np 


def next_turn(row, col):

    global single_player 

    if list_btn[row][col]['text']  == "" and check_winner() is False: 
        if single_player == players[0]:
            list_btn[row][col]['text'] = single_player 

            #If there is no winner it is the other player's turn and it goes on like this until one wins
            if check_winner() is False:
                single_player = players[1]
                label.config(text = (players[1] + " turn"))
            
            #Winning case
            elif check_winner() is True:
                label.config(text = (players[0] + " wins"))
            
            #Tie case
            elif check_winner() == "Tie":
                label.config(text = ("Tie!"))

        #if it is not player[0]'s turn then it is player[1]'s turn
        else: 

            list_btn[row][col]['text'] = single_player

            #If there is no winner it is the other player's turn and it goes on like this until one wins
            if check_winner() is False:
                single_player = players[0]
                label.config(text = (players[0] + " turn"))
            
            #Winning case
            elif check_winner() is True:
                label.config(text = (players[1] + " wins"))
            
            #Tie case
            elif check_winner() == "Tie":
                label.config(text = ("Tie!"))

#check_empy ==> checks that all elements are equal and none is ‘’ empty string
def check_empty(lista):
    values = set(lista)
    return len(values) == 1 and "" not in values 

#check_winner() ==> check all win conditions
def check_winner():
    for row in range(len(list_btn)):

        if list_btn[row][0]['text'] == list_btn[row][1]['text'] == list_btn[row][2]['text'] != "":

            list_btn[row][0].config(highlightbackground="green",highlightcolor="green", highlightthickness=2) #cosi funziona ma riempe solo il bordo
            list_btn[row][1].config(highlightbackground="green",highlightcolor="green", highlightthickness=2)
            list_btn[row][2].config(highlightbackground="green",highlightcolor="green", highlightthickness=2)

            return True
    
    for col in range(len(list_btn[0])):
        if list_btn[0][col]['text'] == list_btn[1][col]['text'] == list_btn[2][col]['text'] != "":

            list_btn[0][col].config(highlightbackground="red",highlightcolor="red", highlightthickness=2)
            list_btn[1][col].config(highlightbackground="red",highlightcolor="red", highlightthickness=2)
            list_btn[2][col].config(highlightbackground="red",highlightcolor="red", highlightthickness=2)

            return True
        
    #To check the diagonals of the matrix I use NUMPY which has methods already defined
    #get main diagonal
    main_diag = np.diag(list_btn).tolist() #cast list
    main_diag_text = [btn.cget("text") for btn in main_diag] #.cget ==> I extract the strings shown on the diagonal btn

    sec_diag = np.diag(np.fliplr(list_btn)).tolist()
    sec_diag_text = [btn.cget("text") for btn in sec_diag]

    #per vedere se tutti elementi sono uguali uso set perché diventa TRUE solo quando tutti gli elementi sono uguali
    if check_empty(main_diag_text):
        for btn in main_diag: 
            btn.config(highlightbackground="black",highlightcolor="black", highlightthickness=2)
        return True
    
    elif check_empty(sec_diag_text):
        for btn in sec_diag:
            btn.config(highlightbackground="black",highlightcolor="black", highlightthickness=2)
        return True
    
    elif empty_space() is False:
        for row in range(len(list_btn)):
            for col in range(len(list_btn[row])):
                list_btn[row][col].config(highlightbackground="purple",highlightcolor="purple", highlightthickness=2)
        return "Tie"
    else:
        return False #when nobody wins and there is no draw


#empty_space ==> is needed inside check_winner() to see if a tie is reached.
#break even is reached when all cells are full and none meet the win condition
def empty_space(): 
    spaces = 9
    for row in range(len(list_btn)):
        for col in range(len(list_btn[row])):
            if list_btn[row][col]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False 
    else:
        return True

def new_game(): 
    global single_player 
    single_player = random.choice(players) 
    label.config(text = single_player + " turn") 

    for row in range(len(list_btn)):
        for col in range(len(list_btn[row])):
            list_btn[row][col].config(text = "", highlightbackground="#F0F0F0",highlightcolor="#F0F0F0", highlightthickness=2)


def create_buttons():

    return [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]


window = Tk()
window.title("Tic Tac Toe by Linari Luca")
players = ["X", "O"] 
single_player = random.choice(players) 
list_btn = create_buttons() 

label = Label(text = single_player + " turn", font=("Verdana",40))
label.pack(side = "top") 

reset_btn = Button(text = "Restart", font = ("Verdana", 20), command = new_game)
reset_btn.pack(side = "top")

#Define frame
frame = Frame(window) 
frame.pack() 

for row in range(len(list_btn)):
    for col in range(len(list_btn[row])):
        list_btn[row][col] = Button(frame, text = "", font = ("Verdana", 40), width = 5, height = 2, 
                                    command = lambda row = row, column = col: next_turn(row, column)) 
        
        list_btn[row][col].grid(row = row, column = col)
            

window.mainloop() 

