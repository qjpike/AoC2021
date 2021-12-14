f = open("input.txt")
dat = [i.strip() for i in f.readlines()]

template = 'NBOKHVHOSVKSSBSVVBCS'
# template = 'NNCB'

pairs = dict()
for i in dat:
    l,r = i.split("->")
    pairs[l.strip()] = r.strip()


for i in range(10):
    ptr = 0
    while ptr < len(template):
        if template[ptr:ptr+2] in pairs.keys():
            template = template[:ptr] + template[ptr] + pairs[template[ptr:ptr+2]] + template[ptr+1:]
            ptr += 1
        ptr += 1


ress = []
for i in list(set(pairs.values())):
    ress.append(template.count(i))

print("1:",max(ress) - min(ress))

template = 'NBOKHVHOSVKSSBSVVBCS'
# template = 'NNCB'

import collections
counts = collections.defaultdict(int)
for i in range(len(template)-1):
    counts[template[i:i+2]] += 1

for i in range(40):
    new_counts = collections.defaultdict(int)
    for k,v in counts.items():
        if k in pairs:
            new_counts[k[0] + pairs[k]] += v
            new_counts[pairs[k] + k[1]] += v
        else:
            new_counts[k] += v
    counts = new_counts

score = collections.defaultdict(int)
for k,v in counts.items():
    score[k[0]] += v
score[template[-1]] += 1

print("2:",max(list(score.values())) - min(list(score.values()))) # 7553107135051 too high; 1466015503702 too low; 3776553567526 too high