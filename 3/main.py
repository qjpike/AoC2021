f = open("input.txt")
dat = [i.strip() for i in f.readlines()]
# dat = [int(i) for i in f.readlines()]
# dat = [i.split() for i in f.readlines()]
# dat = ''

def get_rating(dat):
    for i,v in enumerate(dat):
            dat[i] = list(v)

    bits_0 = [0]*len(dat[0])
    bits_1 = [0]*len(dat[0])

    for j in dat:
        for i,v in enumerate(j):
            if v == '1':
                bits_1[i] += 1
            else:
                bits_0[i] += 1

    gamma = ''
    epsilon = ''
    for i,v in enumerate(bits_0):
        if v > bits_1[i]:
            gamma += '0'
            epsilon += '1'
        elif v < bits_1[i]:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '1'
            epsilon += '0'


    return (int(gamma,2),int(epsilon,2))

g,e = get_rating(dat)
print("1:",e*g)

def count_pos(inp,pos):
    z = 0
    o = 0
    for i in inp:
        if i[pos] == '0':
            z += 1
        else:
            o += 1

    return z,o

def eliminate(inp, rating):
    z = 0
    while len(inp) > 1:
        zero,one = count_pos(inp,z)
        if rating == 1:
            if zero > one:
                r = 0
            else:
                r = 1
        else:
            if one < zero:
                r = 1
            else:
                r = 0
        next = []
        for j,k in enumerate(inp):
            if k[z] == str(r):
                next.append(inp[j])
        inp = next
        z += 1

    return inp

import copy

o2_arr = copy.deepcopy(dat)
o2 = int(''.join(eliminate(o2_arr,1)[0]),2)

co2_arr = copy.deepcopy(dat)
co2 = int(''.join(eliminate(co2_arr,0)[0]),2)


print("2:",o2*co2) # 10336170 wrong 16769025 16740360