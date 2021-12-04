
import numpy

f = open("input.txt")
# dat = [i.strip() for i in f.readlines()]
# dat = [int(i) for i in f.readlines()]
dat = [i.split() for i in f.readlines()]
# dat = ''


draws = [87,7,82,21,47,88,12,71,24,35,10,90,4,97,30,55,36,74,19,50,23,46,13,44,69,27,2,0,37,33,99,49,77,15,89,98,31,51,22,96,73,94,95,18,52,78,32,83,85,54,75,84,59,25,76,45,20,48,9,28,39,70,63,56,5,68,61,26,58,92,67,53,43,62,17,81,80,66,91,93,41,64,14,8,57,38,34,16,42,11,86,72,40,65,79,6,3,29,60,1]
# draws = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
boards = []

def check_board(b):
    for i in b:
        if sum(i) == -5:
            return True
    b_t = numpy.transpose(b)
    for i in b_t:
        if sum(i) == -5:
            return True
    return False


for i in dat:
    if len(i) > 1:
        boards.append(i)
#to print all boards (debug)
# for i in range(len(boards)):
#     if i % 5 == 0:
#         print(" ")
#     else:
#         print(boards[i])

for i,b in enumerate(boards):
    for j,k in enumerate(b):
        boards[i][j] = int(k)

found = False
for i in draws:
    for index,j in enumerate(boards):
        if i in j:
            boards[index][boards[index].index(i)] = -1

    for k in range(0,len(boards),5):
        if check_board(boards[k:k+5]):
            cnt = 0
            for z in boards[k:k+5]:
                for r in z:
                    if r != -1:
                        cnt += r
            print("1:",i*cnt)
            found = True
            break
    if found:
        break

#87912
#87417

boards = []

for i in dat:
    if len(i) > 1:
        boards.append(i)

for i,b in enumerate(boards):
    for j,k in enumerate(b):
        boards[i][j] = int(k)

found = False
for i in draws:
    for index,j in enumerate(boards):
        if i in j:
            boards[index][boards[index].index(i)] = -1

    b_cntr = 0
    while b_cntr < len(boards):
        if check_board(boards[b_cntr:b_cntr+5]):
            if len(boards) == 5:
                found = True
            elif not found:
                del(boards[b_cntr:b_cntr+5])
        else:
            b_cntr += 5

        if found:
            break

    if found:
        break

cnt = 0
for z in boards[0:5]:
    for r in z:
        if r != -1:
            cnt += r

print("2:",i * cnt)

#18368
