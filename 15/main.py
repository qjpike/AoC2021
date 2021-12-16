f = open("input.txt")
dat = [i.strip() for i in f.readlines()]

dirs = [(1,0),(0,-1),(-1,0),(0,1)]

field = dict()
for y,st in enumerate(dat):
    for x,ch in enumerate(st):
        field[(x,y)] = int(ch)

x_max = x
y_max = y
x_max1 = x

import collections
q = collections.deque()
q.append((0,0))


def default():
    return 1000000

scores = collections.defaultdict(default)
scores[(0,0)] = 0
while len(q) > 0:
    x,y = q.popleft()
    for nx,ny in dirs:
        if (x+nx,y+ny) in field and scores[(x,y)] + field[(x+nx,y+ny)] < scores[(x+nx,y+ny)]:
            scores[(x+nx,y+ny)] = scores[(x,y)] + field[(x+nx,y+ny)]
            q.append((x+nx,y+ny))

print("1:",scores[(x_max,y_max)])


import time
tic = time.perf_counter()

for y in range(y_max+1):
    for i in range(5):
        for j in range(1,x_max+1):
            field[(x_max + j + i*x_max,y)] = field[(j+i*x_max-1,y)] + 1 if field[(j+i*x_max-1,y)] < 9 else 1

for i in range(5):
    for y in range(y_max+1):
        for j in range((x_max+1)*5):
            field[(j, y + i*(y_max+1) + y_max + 1)] = field[(j, y + i*(y_max+1))] + 1 if field[(j, y + i*(y_max+1))] < 9 else 1


x_max = (x_max + 1) * 5
y_max = (y_max + 1) * 5

q = collections.deque()
q.append((0,0))
scores = collections.defaultdict(default)
scores[(0,0)] = 0
while len(q) > 0:
    x,y = q.popleft()
    for nx,ny in dirs:
        if (x+nx,y+ny) in field and scores[(x,y)] + field[(x+nx,y+ny)] < scores[(x+nx,y+ny)]:
            scores[(x+nx,y+ny)] = scores[(x,y)] + field[(x+nx,y+ny)]
            q.append((x+nx,y+ny))

print("2:",scores[(x_max-1,y_max-1)])

toc = time.perf_counter()

# part 2 is a long runtime - over a minute.
print("Runtime:",toc-tic,"seconds")