from inspect import currentframe
from game import BOARD, free_spaces

# Unit tests #
TEST_COUNTER = 0
ERRORS = {}

def add_errors(func, msg):
    ERRORS[func] = msg

def test_free_spaces():
    print('.free_spaces given empty board should return collection of all possible coords')
    TEST_COUNTER + 1
    # setup known good values
    collection_of_all_coords = []

    for i in range(0, 2):
        for n in range(0, 2):
            collection_of_all_coords.append((i, n))
            # [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]

    # setup values from app
    board1 = BOARD # copy? clone?
    free = free_spaces(board1)

    # assertion
    if(free == collection_of_all_coords):
        print('pass')
    else:
        print('fail')
        add_errors(currentframe().f_code.co_name,'failed! Board wasn\'t empty')

    # output
    # print(res)

def run_unit_tests():
    print('\n\n***** Unit Tests ******\n\n')
    test_free_spaces()

    # print errors:
    for k, v in ERRORS.items():
        print('error! {k}: {v}'.format(k=k, v=v))

# test stats
def test_stats():
    print(TEST_COUNTER)
    print('tests complete')
# Integration tests #
