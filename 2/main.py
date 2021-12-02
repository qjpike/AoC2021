f = open("input.txt")
# dat = [i.strip() for i in f.readlines()]
# dat = [int(i) for i in f.readlines()]
dat = [i.split() for i in f.readlines()]
# dat = ''

moves = ['forward','down','up']
moves_dir = [(1,0),(0,1),(0,-1)]

pos = (0,0)
for m,a in dat:
    x,y = pos
    mx,my = moves_dir[moves.index(m)]
    pos = (x + int(a)*mx, y + int(a)*my)


print(pos[0]*pos[1])

pos = (0,0)
angle = 0
for m,a in dat:
    x,y = pos
    if m == 'up':
        angle -= int(a)
    elif m == 'down':
        angle += int(a)
    if m == 'forward':
        pos = (x + int(a),y + int(a)*angle)

print(pos[0]*pos[1]) # wrong 3487435318
