# import 'math'
# for pretty printing a matrix...
import numpy as np

CONSTANTS = {}
START_INSTRUCTIONS = 'run game.new_game() to start'

print(START_INSTRUCTIONS)

# no tests!
def start_game(board, current, winning_combos):
    # player_moves = ['','','','','','','','','','']
    turn = 0
    while(turn < 9):
        # make sure to set empty strings for non-filled spaces, otherwise out of range error
        take_turn(board, current)
        turn += 1
        winner, sequence = check_for_winner(board, winning_combos, current)

        if not winner:
            if not check_for_draw(board, winning_combos):
                # keep playing
                current = switch_player(current)
            else:
                print(f"Draw! {CONSTANTS['restart_instructions']}")
                break
        else:
            # winner!
            print(f"{CONSTANTS['restart_instructions']}")
            break

# no tests!
def take_turn(board, current):
    '''taking a turn'''
    free_space_array = free_spaces(board)
    #i = math.ran(len(free_space_array))
    res_string = input(f"{current}, what space would you like? spaces available: {free_space_array}")
    x,y = res_string.split(",")
    # beep boop beep
    board[int(x)][int(y)] = current
    # or use insert?
    print(f'board is now\n {np.matrix(board)}')
    # puts(f'board is now {board}')
    # each turn:
    #  - if open space...
    #  - play in open space x
    #  - play in open space o

def check_for_winner(board, winningCombos, player):
    ''' check board for winner. returns True or False, and winning sequence if there is one '''
    # use count to see if >= 3 of player?

    # if board contains any winningCombos ?
    # need current_player_board: 2d array of where player tokens are
    winner = False
    sequence = None
    current_player_board = get_player_positions(board, player)

    for combo in winningCombos:
        # is [0,1,2] in array of indexes of 'X'? [0,1,2,4,8]
        if(combo[0] in current_player_board and combo[1] in current_player_board and combo[2] in current_player_board):
            winner = True
        else:
            winner = False
        if(winner):
            sequence = combo
            print(f'Winner! {player} won with {sequence}: {board}')#.format(player=player, board=board))
            break
    return [winner, sequence]

# attempting to have this functional...
# ...but it could easily be refactored and slimmed down if we know where we are in the game flow
# ...based on no winner / turn count
def check_for_draw(board, winningCombos):
    new_board = get_1d_board(board)
    # remove empty spaces
    while(new_board.count('') > 0):
        new_board.remove('')

    if(len(new_board) == 9):
        # look at every combo...is there a winner?
        for combo in winningCombos:
            if(new_board[combo[0]] == new_board[combo[1]] == new_board[combo[2]]):
                # winner!
                # TODO: check for winner here, instead of calling multiple funcs?
                return False
        else:
            return True
    else:
        return False

def get_player_positions(board, player):
    '''creates and returns 1d board of player indexes'''
    new_board = [] # 1d board
    for r, row in enumerate(board):
        for s, space in enumerate(row):
            if space == player:
                index = 0
                if r == 0:
                    index += 0
                elif r == 1:
                    index += 3
                elif r == 2:
                    index += 6

                new_board.append(index + s)
    return new_board

def get_1d_board(board):
    '''creates and returns 1d board of player tokens at indexes'''
    new_board = [] # 1d board
    for r, row in enumerate(board):
        for s, space in enumerate(row):
            index = 0
            if r == 0:
                index += 0
            elif r == 1:
                index += 3
            elif r == 2:
                index += 6

            new_board.insert(index + s, space)
    return new_board

def free_spaces(board):
    free = []
    # loop through each spot on the board array
    # return an array of the free coordinates to choose from
    for r in range(0, 3): #(r = 0; r < 3; r++):
        for c in range(0, 3):#(c = 0; c < 3; c++):
            if (board[r][c] == ''):
                free.append((r, c))
    return free

def switch_player(current):
    if(current == CONSTANTS['players'][0]):
        return CONSTANTS['players'][1]
    else:
        return CONSTANTS['players'][0]

def reset_game():
    _setup()
    return 'reset...'

def _setup():
    CONSTANTS['players'] = [input("Player 1:"), input("Player 2:")]
    CONSTANTS['current_player'] = CONSTANTS['players'][0]
    CONSTANTS['winning_combos'] = winning_combos()
    CONSTANTS['restart_instructions'] = START_INSTRUCTIONS.replace('start','restart')
    CONSTANTS['board'] = [
        ['','',''],
        ['','',''],
        ['','','']
    ]

def play():
    start_game(CONSTANTS['board'], CONSTANTS['current_player'], CONSTANTS['winning_combos'])

def new_game():
    reset_game()
    play()

def winning_combos():
    return [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
