'''
create a magic square of size 4 with specified parameters
from https://www.grogono.com/magic/4x4.php
'''
def create_square(params: list):
    patterns = [[None] for _ in range(5)]
    '''
    pattern 1
    0011
    1100
    0011
    1100
    '''
    pattern_1_1 = [0, 0, 1, 1]
    pattern_1_2 = [1, 1, 0, 0]
    patterns[0] = [[pattern*params[0] for pattern in pattern_1_1],
                [pattern*params[0] for pattern in pattern_1_2],
                [pattern*params[0] for pattern in pattern_1_1],
                [pattern*params[0] for pattern in pattern_1_2]]
    '''
    pattern 2
    0110
    1001
    0110
    1001
    '''
    pattern_2_1 = [0, 1, 1, 0]
    pattern_2_2 = [1, 0, 0, 1]
    patterns[1] = [[pattern*params[1] for pattern in pattern_2_1],
                [pattern*params[1] for pattern in pattern_2_2],
                [pattern*params[1] for pattern in pattern_2_1],
                [pattern*params[1] for pattern in pattern_2_2]]
    '''
    pattern 3
    0101
    0101
    1010
    1010
    '''
    pattern_3_1 = [0, 1, 0, 1]
    pattern_3_2 = [1, 0, 1, 0]
    patterns[2] = [[pattern*params[2] for pattern in pattern_3_1],
                [pattern*params[2] for pattern in pattern_3_1],
                [pattern*params[2] for pattern in pattern_3_2],
                [pattern*params[2] for pattern in pattern_3_2]]
    '''
    pattern 4
    0101
    1010
    1010
    0101
    '''
    patterns[3] = [[pattern*params[3] for pattern in pattern_3_1],
                [pattern*params[3] for pattern in pattern_3_2],
                [pattern*params[3] for pattern in pattern_3_2],
                [pattern*params[3] for pattern in pattern_3_1]]
    '''
    pattern5
    1111
    1111
    1111
    1111
    '''
    patterns[4] = [[params[4] for _ in range(4)] for _ in range(4)]
    square = [[0 for _ in range(4)] for _ in range(4)]
    for pattern in patterns:
        for i in range(4):
            for j in range(4):
                square[i][j] += pattern[i][j]
    return square

sq = create_square([8, 4, 2, 1, 1])
for l in sq:
    print(l)
