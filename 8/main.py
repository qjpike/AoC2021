f = open("input.txt")
# dat = [i.strip() for i in f.readlines()]
# dat = [int(i) for i in f.readlines()]
dat = [i.split() for i in f.readlines()]
# dat = ''

display = ['abcefg','cf','acdeg','acdfg','bcdf','abdfg','abdefg','acf','abcdefg','abcdfg']

count = 0
for i in dat:
    for j in range(i.index("|"),i.__len__()):
        if len(i[j]) in [2,3,4,7]:
            count += 1

print("1:",count)


possibilities = {'a','b','c','d','e','f','g'}

display = [{'a','b','c','e','f','g'},{'c','f'},{'a','c','d','e','g'},{'a','c','d','f','g'},
           {'b','c','d','f'},{'a','b','d','f','g'},{'a','b','d','e','f','g'},{'a','c','f'},
           {'a','b','c','d','e','f','g'},{'a','b','c','d','f','g'}]
outputs = []
for i in dat:
    new_i = i
    # key is decoded, value is encoded
    decoder = {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None}
    while len(''.join(new_i)) != len(i): #TODO: need better loop exit
        for j,k in enumerate(i):
            if len(k) == 2:
                # value is 1
                decoder[1] = set(k)
                new_i[j] = '1'
            elif len(k) == 4:
                # value is 4
                decoder[4] = set(k)
                new_i[j] = '4'
            elif len(k) == 3:
                # value is 7
                decoder[7] = set(k)
                new_i[j] = '7'
            elif len(k) == 7:
                # value is 8, can't decifer anything though
                decoder[8] = set(k)
                new_i[j] = '8'
            if decoder[1] and decoder[4] and decoder[7]:
                if len(k) == 5:
                    if len(set(k) & decoder[4]) == 2 and len(set(k) & decoder[7]) == 2 and len(set(k) & decoder[1]) == 1:
                        # value is 2
                        decoder[2] = set(k)
                        new_i[j] = '2'
                    elif len(set(k) & decoder[1]) == 2 and len(set(k) & decoder[4]) == 3 and len(set(k) & decoder[7]) == 3:
                        # value is 3
                        decoder[3] = set(k)
                        new_i[j] = '3'
                    elif len(set(k) & decoder[1]) == 1 and len(set(k) & decoder[4]) == 3 and len(set(k) & decoder[7]) == 2:
                        # value is 5
                        decoder[5] = set(k)
                        new_i[j] = '5'
                elif len(k) == 6:
                    if len(set(k) & decoder[1]) == 2 and len(set(k) & decoder[4]) == 3 and len(set(k) & decoder[7]) == 3:
                        # value is 0
                        decoder[0] = set(k)
                        new_i[j] = '0'
                    elif len(set(k) & decoder[1]) == 1 and len(set(k) & decoder[4]) == 3 and len(set(k) & decoder[7]) == 2:
                        # value is 6
                        decoder[6] = set(k)
                        new_i[j] = '6'
                    elif len(set(k) & decoder[1]) == 2 and len(set(k) & decoder[4]) == 4 and len(set(k) & decoder[7]) == 3:
                        # value is 9
                        decoder[9] = set(k)
                        new_i[j] = '9'
    outputs.append(int(''.join(new_i)[new_i.index("|")+1:]))
print("2:",sum(outputs))
