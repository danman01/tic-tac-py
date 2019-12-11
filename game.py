import numpy as np # for pretty printing a matrix...
import time

CONSTANTS = {}
START_INSTRUCTIONS = 'run game.new_game() to start'

print(START_INSTRUCTIONS)

# no tests #
def start_game(board, current, winning_combos):
    turn = 0
    while(turn < 9):
        # make sure to set empty strings for non-filled spaces, otherwise out of range error
        print(f'turn {turn}:')
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
    '''taking a turn using input prompt'''
    free_space_array = free_spaces(board)

    # import random
    #
    # print("Where should I move?")
    # cities = ["Seattle", "Portland", "San Francisco", "Vancouver"]
    # city = random.choice(cities)
    # print("That's it. I'm moving to", city)
    cpus_turn = (CONSTANTS['cpu'] and current == CONSTANTS['players'][1])
    if(CONSTANTS['ai'] or cpus_turn):
        import random
        x,y = random.choice(free_space_array)
        print(f'{current}\'s turn. Waiting for cpu...')
        time.sleep( random.choice(range(1,3)) )
        print(f'{current} choze {x},{y}')
    else:
        # try some error handling...
        while True:
            try:
                choice = input(f"{current}, what space would you like? spaces available: {free_space_array}")
                x,y = choice.split(",")
                # TODO: ensure space is actually free...
                board[int(x)][int(y)] = current
                # or use insert?
            except ValueError:
                print('try again...use the format 2,2 or 0,0')
                continue
            except IndexError:
                print('try again...make sure to stay within limits!')
                continue
            except Exception:
                print('what did you do?!?!?!')
                raise
            break

    board[int(x)][int(y)] = current
    print(f'board is now\n {np.matrix(board)}')

def check_for_winner(board, winningCombos, player):
    ''' check board for winner. returns True or False, and winning sequence if there is one '''
    # use count to see if >= 3 of player?

    winner = False
    sequence = None
    current_player_board = get_1d_board(board, player)

    for combo in winningCombos:
        # ex: is [0,1,2] in array of indexes of 'X'? [0,1,2,4,8]
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
# could be refactored and slimmed down if we know where we are in the game flow
# based on no winner / turn count
def check_for_draw(board, winningCombos):
    draw = False
    new_board = get_1d_board(board)

    # remove empty spaces. easier way?
    while(new_board.count('') > 0):
        new_board.remove('')

    if(len(new_board) == 9):
        # look at every combo...is there a winner?
        for combo in winningCombos:
            if(new_board[combo[0]] == new_board[combo[1]] == new_board[combo[2]]):
                # winner!
                # TODO: check for winner here, instead of calling multiple funcs?
                break
        else:
            # no winners?
            draw = True
    return draw

def get_1d_board(board, player=None):
    '''creates and returns 1d board of player tokens at indexes. Pass a player token to insert the token at index'''
    new_board = []
    for r, row in enumerate(board):
        for s, space in enumerate(row):
            index = 0
            if r == 0:
                index += 0
            elif r == 1:
                index += 3
            elif r == 2:
                index += 6

            if(player and space == player):
                # just record the index of the player
                new_board.append(index + s)
            elif(not player):
                new_board.insert(index + s, space)
    return new_board

def free_spaces(board):
    free = []
    # loop through each spot on the board array
    # return an array of the free coordinates to choose from
    # will be more useful for AI
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

def reset_game(ai, cpu):
    _setup(ai, cpu)
    return 'reset...'

def _setup(ai, cpu):
    CONSTANTS['players'] = [input("Player 1:"), input("Player 2:")]
    CONSTANTS['current_player'] = CONSTANTS['players'][0]
    CONSTANTS['winning_combos'] = winning_combos()
    CONSTANTS['ai'] = ai
    CONSTANTS['cpu'] = cpu
    CONSTANTS['start_time'] = time.ctime()
    CONSTANTS['end_time'] = None
    CONSTANTS['restart_instructions'] = START_INSTRUCTIONS.replace('start','restart')
    CONSTANTS['board'] = [
        ['','',''],
        ['','',''],
        ['','','']
    ]

def play():
    start_game(CONSTANTS['board'], CONSTANTS['current_player'], CONSTANTS['winning_combos'])

def new_game(ai=False, cpu=False):
    reset_game(ai, cpu)
    play()

def winning_combos():
    return [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
