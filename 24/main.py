# with help from: https://github.com/dphilipson/advent-of-code-2021/blob/master/src/days/day24.rs

# index       0   1   2    3     4    5   6   7    8   9  10  11   12  13
# div    =  [ 1,  1,  1,   1,   26,  26,  1,  1,  26, 26,  1, 26,  26, 26]
# check  =  [13, 12, 12,  10,  -11, -13, 15, 10,  -2, -6, 14,  0, -15, -4]
# offset =  [ 8, 13,  8,  10,   12,   1, 13,  5,  10,  3,  2,  2,  12,  7]
#
# push w[0] + 8                                                           1       5
# push w[1] + 13                                                          3       9
# push w[2] + 8                                                           6       9
# push w[3] + 10                                                          2       9
# pop. must have w[4] == popped_value - 11    -> w[4] == w[3] - 1         1       8
# pop. must have w[5] == popped_value - 13    -> w[5] == w[2] - 5         1       4
# push w[6] + 13                                                          1       2
# push w[7] + 5                                                           1       6
# pop. must have w[8] == popped_value - 2     -> w[8] == w[7] + 3         4       9
# pop. must have w[9] == popped_value - 6     -> w[9] == w[6] + 7         8       9
# push w[10] + 2                                                          1       7
# pop. must have w[11] == popped_value        -> w[11] == w[10] + 2       3       9
# pop. must have w[12] == popped_value - 15   -> w[12] == w[1] - 2        1       7
# pop. must have w[13] == popped_value - 4    -> w[13] == w[0] + 4        5       9
#
#
# Part 1: 59998426997979
# Part 2: 13621111481315

