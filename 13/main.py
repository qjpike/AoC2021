f = open("input.txt")
dat = set((int(i.strip().split(",")[0]),int(i.strip().split(",")[1])) for i in f.readlines())

max_x = max(i[0] for i in dat)
max_y = max(i[1] for i in dat)

def find_points(axis, ind):
     res = []
     for x,y in dat:
         if axis == 'x':
             if x > ind:
                 res.append((x,y))
         else:
             if y > ind:
                 res.append((x,y))
     return res

f = open("folds.txt")
folds = [(i.strip().split("=")[0][-1],int(i.strip().split("=")[1])) for i in f.readlines()]

# to fold, keep the dots on the same row/column and move the same distance to the opposite side of the fold line
first = True
for d,ind in folds:
    folded = find_points(d,ind)
    for x,y in folded:
        if d == 'y':
            dat.add((x,ind-(y-ind)))
        elif d == 'x':
            dat.add((ind-(x-ind),y))
        dat.remove((x,y))

    # it was just printing all of them, so this cleans it up.
    if first:
        print("1:",len(dat)) # 958 wrong
        first = False

max_x = max(i[0] for i in dat)
max_y = max(i[1] for i in dat)

for i in range(0,max_y+1):
    for j in range(0,max_x+1):
        if (j,i) in dat:
            print(chr(0x2588),end='')
        else:
            print(" ",end='')
    print("")