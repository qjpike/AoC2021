f = open("input.txt")
# dat = [i.strip() for i in f.readlines()]
# dat = [int(i) for i in f.readlines()]
# dat = [i.split() for i in f.readlines()]
# dat = ''

dat = [int(i) for i in f.read().split(",")]


def count_fish(cycles):
    fish = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

    for i in dat:
        fish[i] += 1

    for j in range(cycles):
        new_fish = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0,8:0}
        for i in fish:
            if i == 0:
                new_fish[8] = fish[i]
                new_fish[6] += fish[i]
            else:
                new_fish[i-1] += fish[i]

        fish = new_fish

    return sum(list(fish.values()))

print("1:",count_fish(80))
print("2:",count_fish(256))
