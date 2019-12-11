from flask import Flask
from inspect import currentframe
from game import CONSTANTS as GAME_CONSTANTS, winning_combos, free_spaces, switch_player, check_for_winner, check_for_draw, get_1d_board, reset_game

app = Flask(__name__)

reset_game()
# Unit tests #
CONSTANTS = {}
print('run_unit_tests() to run tests...pass debug=true to turn on debugger when error')
def test_setup(debug):
    CONSTANTS['test_results']=[]
    CONSTANTS['errors'] = {}
    CONSTANTS['new_game_board'] = [
        ['','',''],
        ['','',''],
        ['','','']
    ]
    CONSTANTS['completed_game'] = [
        ['X','X','O'],
        ['X','X','O'],
        ['O','O','X']
    ]
    CONSTANTS['draw_game'] = [
        ['O','X','O'],
        ['X','X','O'],
        ['O','O','X']
    ]
    CONSTANTS['incomplete_game'] = [
        ['O','X','O'],
        ['X','X',''],
        ['O','','']
    ]
    if(debug):
        CONSTANTS['debug'] = True
    else:
        CONSTANTS['debug'] = False

    return 'setup complete'

def add_errors(func, msg):
    CONSTANTS['errors'][func] = msg

def get_meth_name(meth_name):
    return meth_name.f_code.co_name.replace('test_','')

def expect_equality(meth, item1, item2):
    print(f'testing {meth}.  .  .   .  ... .. ...')
    if (item1 == item2):
        CONSTANTS['test_results'].append(True)
        print('passed!')
    else:
        CONSTANTS['test_results'].append(False)
        msg = f'failed! item1 {item1} does not match {item2}'#.format(item1=item1, item2=item2)
        add_errors(meth, msg)
        if(CONSTANTS['debug'] == True):
            # import pdb; pdb.set_trace()
            breakpoint()

def test_check_for_winner(board, winningCombos, player):
    meth = get_meth_name(currentframe())
    print(f'{meth} determine if there is a winner, and what winning sequence is')#.format(meth=meth))
    winner, sequence = check_for_winner(board, winningCombos, player)
    correct_sequence = [0,4,8]
    expect_equality(meth, winner, True)
    expect_equality(meth, sequence, correct_sequence)

def test_check_for_draw(board, winningCombos):
    meth = get_meth_name(currentframe())
    print(f'{meth} determine if there is a draw')#.format(meth=meth))
    result = check_for_draw(board, winningCombos)
    expect_equality(meth, result, True)

def test_check_for_no_draw(board, winningCombos):
    meth = get_meth_name(currentframe())
    print(f'{meth} determine if there is not a draw')#.format(meth=meth))
    result = check_for_draw(board, winningCombos)
    expect_equality(meth, result, False)

def test_get_player_positions(board, player):
    meth = get_meth_name(currentframe())
    print(f'{meth} return indexes where player tokens are')#.format(meth=meth))
    current_board = get_1d_board(board, player)
    test_board_x_indexes = [0,1,3,4,8]
    expect_equality(meth, current_board, test_board_x_indexes)

def test_switch_player():
    meth = get_meth_name(currentframe())
    print(f'{meth} should switch CURRENT_PLAYER from x to o, or o to x')#.format(meth=meth))
    player = 'X'
    correct_new_player = 'O'
    new_player = switch_player(player)
    expect_equality(meth, new_player, correct_new_player)

def test_free_spaces():
    meth = get_meth_name(currentframe())
    print(f'{meth} given empty board should return collection of all possible coords')#.format(meth=meth))
    # setup known good values
    collection_of_all_coords = []

    # buggy...just hardcode it!
    for i in range(0, 3):
        for n in range(0, 3):
            collection_of_all_coords.append((i, n))
            # [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]

    # setup values from app
    board1 = CONSTANTS['new_game_board'] # copy? clone?
    free = free_spaces(board1)

    # assertion
    expect_equality(meth, free, collection_of_all_coords)

def test_get_1d_board(board):
    meth = get_meth_name(currentframe())
    print(f'{meth} get 1d board from gameboard')#.format(meth=meth))
    new_board = get_1d_board(board)
    # based on looking at passed in board...
    correct_1d_board = ['X','X','O','X','X','O','O','O','X']
    expect_equality(meth, new_board, correct_1d_board)

def test_reset_game():
    meth = get_meth_name(currentframe())
    print(f'{meth} resetting game and game constants')
    board = GAME_CONSTANTS['board']
    fresh_board = [
        ['','',''],
        ['','',''],
        ['','','']
    ]
    reset_game()
    free_spaces_array = free_spaces(board)
    expect_equality(meth, get_1d_board(board), get_1d_board(fresh_board))
    expect_equality(meth, len(free_spaces_array), 9)

@app.route("/test")
def run_unit_tests(debug = False):
    html = '\n***** Unit Tests ******\n'
    html += test_setup(debug)
    # todo:
    # test_start_game()
    # test_take_turn()
    test_free_spaces()
    test_switch_player()
    test_get_player_positions(CONSTANTS['completed_game'], 'X')
    test_check_for_winner(CONSTANTS['completed_game'], winning_combos(), 'X')
    test_check_for_draw(CONSTANTS['draw_game'], winning_combos())
    test_check_for_no_draw(CONSTANTS['incomplete_game'], winning_combos())
    test_get_1d_board(CONSTANTS['completed_game'])
    test_reset_game()


    # print errors:
    html += "\n**** errors: **** \n"
    for k, v in CONSTANTS['errors'].items():
        html += f'error! {k}: {v}'#.format(k=k, v=v)

    html += test_stats()
    print(html)


# test stats
def test_stats():
    str = '\n***** Unit Test Stats ******\n'
    str += '{passed} passed. {failed} failed'.format(passed=CONSTANTS['test_results'].count(True), failed=CONSTANTS['test_results'].count(False))
    str += 'tests complete'
    return str

# flask
if __name__ == "__main__":
    app.run()
