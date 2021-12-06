f = open("input.txt")
dat = [i.split() for i in f.read().split("\n")]

def print_field(field):
    for i in range(10):
        for j in range(10):
            if (j,i) in field:
                print(field[(j,i)],end="")
            else:
                print(".",end="")
        print("")


def fill_field(p2=False):
    field = dict()
    for i in dat:
         start = i[0].split(",")
         end = i[2].split(",")

         if start[0] == end[0]:
             # this is i a vertical line
             x = int(start[0])
             y1 = int(start[1]) if int(start[1]) < int(end[1]) else int(end[1])
             y2 = int(end[1]) if y1 == int(start[1]) else int(start[1])
             for j in range(y1,y2+1):
                 if (x,j) not in field:
                     field[(x,j)] = 0
                 field[(x,j)] += 1
         elif start[1] == end[1]:
            # this is a horizontal line
            y = int(start[1])
            x1 = int(start[0]) if int(start[0]) < int(end[0]) else int(end[0])
            x2 = int(end[0]) if x1 == int(start[0]) else int(start[0])
            for j in range(x1,x2+1):
                if (j,y) not in field:
                    field[(j,y)] = 0
                field[(j,y)] += 1
         elif abs(int(start[0]) - int(end[0])) == abs(int(start[1]) - int(end[1])) and p2:
            y1 = int(start[1]) if int(start[1]) < int(end[1]) else int(end[1])
            y2 = int(end[1]) if y1 == int(start[1]) else int(start[1])
            x1 = int(start[0]) if y1 == int(start[1]) else int(end[0])
            x2 = int(end[0]) if y2 == int(end[1]) else int(start[0])
            if x1 < x2:
                slope = 1
            else:
                slope = -1
            for j,k in enumerate(range(y1,y2+1)):
                pos = (x1 + j*slope,k)
                if pos not in field:
                    field[pos] = 0
                field[pos] += 1

    print_field(field)
    count = 0
    for i in list(field.values()):
        if i > 1:
            count += 1

    return count


print("1:",fill_field())
print("2:",fill_field(True)) # 108605 Too high #108216 too high