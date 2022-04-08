import os
from termcolor import colored

def board_1(state):
    for i in range(len(state)):
        if state[i] == "x":
            state[i] = colored("x", "magenta")
        elif state[i] == "O":
            state[i] = colored("O", "green")
    a1, a2, a3, a4, a5, a6, a7, a8, a9 = state[0], state[1], state[2], state[3], state[4], state[5], state[6], state[7], state[8]
    print(a7,"|",a8,"|",a9)
    print("--|---|--")
    print(a4,"|",a5,"|",a6)
    print("--|---|--")
    print(a1,"|",a2,"|",a3)

def board_2(state):
    for i in range(len(state)):
        if state[i] == "x":
            state[i] = colored("x", "magenta")
        elif state[i] == "O":
            state[i] = colored("O", "green")
    a1, a2, a3, a4, a5, a6, a7, a8, a9 = state[0], state[1], state[2], state[3], state[4], state[5], state[6], state[7], state[8]
    print(a7,"█",a8,"█",a9)
    print("▃▃█▃▃▃█▃▃")
    print(a4,"█",a5,"█",a6)
    print("▃▃█▃▃▃█▃▃")
    print(a1,"█",a2,"█",a3)

def board(state, board_choice):
    if board_choice == 1:
        board_2(state)
    else:
        board_1(state)

def win_cond(state, game_done):
    for i in range(len(state)):
        if state[0] == state[1] == state[2]:
            game_done = True
        if state[3] == state[4] == state[5]:
            game_done = True
        if state[6] == state[7] == state[8]:
            game_done = True
        if state[0] == state[3] == state[6]:
            game_done = True
        if state[1] == state[4] == state[7]:
            game_done = True
        if state[2] == state[5] == state[8]:
            game_done = True
        if state[0] == state[4] == state[8]:
            game_done = True
        if state[2] == state[4] == state[6]:
            game_done = True
        global gd
        gd = game_done

def inp(player, state):
    if player == 'x':
        print(colored('x : make your choice!', 'magenta'))
    else:
        print(colored('O : make your choice!', 'green'))
    z = int(input())
    if type(state[z-1]) == int:
        state[z-1] = player
    else:
        print('wrong u fuk tard')
        print('try again')
        inp(player, state)


def game():
    board_choice = int(input('Thicc Board = 1\nThin Board = 2\n'))
    state = [1,2,3,4,5,6,7,8,9]
    game_done = win_cond(state, False)
    iswinner = False
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(10):
        board(state,board_choice)
        win_cond(state, game_done)
        if gd:
            if i%2 == 0:
                print(colored('Player 2 won', 'green'))
                iswinner = True
                break
            else:
                print(colored('Player 1 won', "magenta"))
                iswinner = True
                break
        if i%2 == 0:
            inp('x', state)
        else:
            inp('O', state)
        os.system('cls' if os.name == 'nt' else 'clear')
    if not iswinner:
        print("There's no winner")
game()
