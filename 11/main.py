f = open("input.txt")
dat = [list(i.strip()) for i in f.readlines()]

surrounds = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]

octo = dict()

for i,j in enumerate(dat):
    for k,l in enumerate(j):
        octo[(k,i)] = int(l)

import collections

count = 0
z = 0
while True:
    flashers = collections.deque()
    done_flashed = set()
    for pos in octo:
        octo[pos] += 1
        if octo[pos] > 9:
            flashers.append(pos)
            done_flashed.add(pos)

    while len(flashers) > 0:
        cur = flashers.popleft()
        x,y = cur
        for i in surrounds:
            nx,ny = i
            if (x+nx,y+ny) in octo and (x+nx,y+ny) not in done_flashed:
                octo[(x+nx,y+ny)] += 1
                if octo[(x+nx,y+ny)] > 9:
                    flashers.append((x+nx,y+ny))
                    done_flashed.add((x+nx,y+ny))

    for i in list(done_flashed):
        octo[i] = 0
    count += len(done_flashed)

    if z == 99:
        print("1:",count)

    if done_flashed == octo.keys():
        print("2:",z+1)
        break
    z += 1