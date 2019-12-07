from game import BOARD, free_spaces

# Unit tests #
print('\n\n***** Unit Tests ******\n\n')
TEST_COUNTER = 0

def run_unit_tests():
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

    # output
    # print(res)

# test stats
def test_stats():
    print(TEST_COUNTER)
    print('tests complete')
# Integration tests #
