f = open('input.txt')
dat = [i.strip() for i in f.readlines()]

dirs = [(0,1),(1,0),(0,-1),(-1,0)]

field = dict()

for y,i in enumerate(dat):
    for x,j in enumerate(i):
        field[(x,y)] = int(j)

lp = []
count = 0
for x,y in field:
    locs = 0
    for nx,ny in dirs:
        if (x+nx,y+ny) in field and  field[(x,y)] < field[(x + nx,y + ny)]:
            locs += 1
        if (x+nx,y+ny) not in field:
            locs += 1
    if locs == 4:
        count += field[(x,y)] + 1
        lp.append((x,y))

print("1:",count)

import collections

def count_basin(pt):

    queue = collections.deque([pt])
    basin_locs = {pt}
    while len(queue) != 0:
        x,y = queue.popleft()
        for nx,ny in dirs:
            if (x+nx, y+ny) in field and field[(x,y)] < field[(x+nx,y+ny)] and field[(x+nx,y+ny)] != 9 and (x+nx,y+ny) not in basin_locs:
                basin_locs.add((x+nx,y+ny))
                queue.append((x+nx,y+ny))

    return len(basin_locs)

basons = []
for i in lp:
    basons.append(count_basin(i))
    basons.sort()
    basons = basons[-3:]

print("2:",basons[0]*basons[1]*basons[2])