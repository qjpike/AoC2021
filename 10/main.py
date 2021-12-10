f = open("input.txt")
dat = [i.strip() for i in f.readlines()]

import collections
opens = ["(","[","<","{"]
closes = [")","]",">","}"]
points = [3,57,25137,1197]
points2 = [1,2,4,3]
count= 0
count2 = []

for i in dat:
    stack = collections.deque()
    valid = True
    for j in i:
        if j in opens:
            stack.append(j)
        else:
            opener = stack.pop()
            if closes[opens.index(opener)] != j:
                count += points[closes.index(j)]
                valid = False
                break
    if valid and len(stack) > 0:
        score = 0
        while len(stack) > 0:
            score *= 5
            val = stack.pop()
            score += points2[opens.index(val)]
        count2.append(score)

print("1:",count) # too high
count2.sort()
print("2:",count2[len(count2)//2])