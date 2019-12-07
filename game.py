# import 'math'

# gameBoard = [
#     [0,1,2],
#     [3,4,5],
#     [6,7,8]
# ]

players = ['x', 'y']

current_player = players[0]

winning_combos = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

# hold game moves
BOARD = [
    ['','',''],
    ['','',''],
    ['','','']
]

def start_game(board, current, winning_combos):
    # player_moves = ['','','','','','','','','','']
    while(len(free_spaces(board)) > 0):
        take_turn(board, current)
        #  - create player index
        #  - check_for_winner
        #  - switch player
        # for i, v in enumerate(board):
        #     if (v == current_player):
        #         player_moves[i] = i # make sure to set empty strings for non-filled spaces, otherwise out of range error
        print(check_for_winner(board, winning_combos, current))
        current_player = switch_player(current)

def take_turn(board, current):
    '''AI taking a turn'''
    free_space_array = free_spaces(board)
    #i = math.ran(len(free_space_array))
    i = (2,1)
    # beep boop beep
    board[i[0]][i[1]] = current
    # each turn:
    #  - if open space...
    #  - play in open space x
    #  - play in open space o

def check_for_winner(board, winningCombos, player):
    # if board contains any winningCombos ?
    # need current_player_board: 2d array of where player tokens are
    winner = ''

    for index, x in enumerate(winningCombos):
        if (board.include(x)):
            print('winner!')
    # for i, x in enumerate(winningCombos):
    #     if (playerIndex[x[0]] == x[0] and playerIndex[x[1] == x[1]] and playerIndex[x[2] == x[2]]):
    #         winner = player
    #         print 'winner!'
    #         break
    return winner

def free_spaces(board):
    free = []
    # loop through each spot on the board array
    # return an array of the free coordinates to choose from
    for r in range(0, 2): #(r = 0; r < 3; r++):
        for c in range(0, 2):#(c = 0; c < 3; c++):
            if (board[r][c] == ''):
                free.append((r, c))
    return free

def switch_player(current):
    if(current == players[0]):
        to_return = players[1]
    else:
        to_return = players[0]
    return to_return


################
### TESTS ######
################
