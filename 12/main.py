f = open("input.txt")
dat = [i.strip() for i in f.readlines()]

ups = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
downs = 'abcdefghijklmnopqrstuvwxyz'

conns = dict()
for i in dat:
    n = i.split("-")
    if n[0] not in conns:
        conns[n[0]] = []
    conns[n[0]].append(n[1])
    if n[1] not in conns:
        conns[n[1]] = []
    conns[n[1]].append(n[0])


def valid_path(path):
    for j,i in enumerate(path):
        if i[0] in downs and i != 'start' and i != 'end':
           if i in path[j+1:]:
               return False
    return True

import collections

q = collections.deque()
s = set()

q.append(['start'])
while len(q) > 0:
    curr = q.pop()
    last = curr[-1]
    for i in conns[last]:
        if i != 'start':
            if i == 'end':
                s.add(tuple(curr+[i]))
            elif valid_path(curr+[i]):
                q.append(curr+[i])

print(len(s))

def valid_path2(path):
    pts = dict()
    for j,i in enumerate(path):
        if i[0] in downs and i != 'start' and i != 'end':
           pts[i] = path.count(i)
    two = 0
    for i in pts.keys():
        if pts[i] > 2:
            return False
        elif pts[i] == 2:
            two += 1

    return two <= 1

import collections

q = collections.deque()
s = set()

q.append(['start'])
while len(q) > 0:
    curr = q.pop()
    last = curr[-1]
    for i in conns[last]:
        if i != 'start':
            if i == 'end':
                s.add(tuple(curr+[i]))
            elif valid_path2(curr+[i]):
                q.append(curr+[i])

print(len(s))

