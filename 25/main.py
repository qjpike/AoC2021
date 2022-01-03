f = open("input.txt")
dat = [i.strip() for i in f.readlines()]

r = (1,0)
d = (0,1)
field = dict()
downs = set()
rights = set()
opens = set()

for y,row in enumerate(dat):
    for x,col in enumerate(row):
        field[(x,y)] = col
        if col == 'v':
            downs.add((x,y))
        elif col == '>':
            rights.add((x,y))
        else:
            opens.add((x,y))

max_x = x+1
max_y = y+1

moves = True
count = 0
while moves:
    moves = False
    new_downs = set()
    new_rights = set()
    new_opens = opens.copy()
    rx,ry = r
    dx,dy = d
    for x,y in list(rights):
        next = ((x+rx) % max_x, (y+ry) % max_y)
        if next in opens:
            # remove new spot from opens, add old spot to opens
            new_opens.remove(next)
            new_opens.add((x,y))
            new_rights.add(next)
            moves = True
        else:
            new_rights.add((x,y))
    opens = new_opens
    new_opens = opens.copy()

    for (x,y) in list(downs):
        next = ((x+dx) % max_x, (y+dy) % max_y)
        if next in opens:
            new_opens.remove(next)
            new_opens.add((x,y))
            new_downs.add(next)
            moves = True
        else:
            new_downs.add((x,y))

    rights = new_rights
    downs = new_downs
    opens = new_opens

    count += 1

print(count)

# Merry Christmas!
