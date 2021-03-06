# 0   1   2   3   4   5   6
#        7   8   9  10
#       11  12  13  14
#       15  16  17  18
#       19  20  21  22
#
from collections import deque

all = set(range(23))
current = { 7:('A',0),  8:('D',0),  9:('C',0), 10:('A',0),\
           11:('D',0), 12:('C',0), 13:('B',0), 14:('A',0),\
           15:('D',0), 16:('B',0), 17:('A',0), 18:('C',0),\
           19:('C',0), 20:('D',0), 21:('B',0), 22:('B',0)}

stacks = dict()
stacks['A'] = deque([('A',0),('D',0),('D',0),('C',0)])
stacks['B'] = deque([('D',0),('C',0),('B',0),('D',0)])
stacks['C'] = deque([('C',0),('B',0),('A',0),('B',0)])
stacks['D'] = deque([('A',0),('A',0),('C',0),('B',0)])
