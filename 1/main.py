f = open("input.txt")
dat = [int(i) for i in f.readlines()]


count = 0
for i in range(len(dat)-1):
    if dat[i+1] > dat[i]:
        count += 1

print("1:",count)

count = 0
for i in range(len(dat)-3):
    if dat[i] + dat[i+1] + dat[i+2] < dat[i+1] + dat[i+2] + dat[i+3]:
        count += 1

print("2:",count)