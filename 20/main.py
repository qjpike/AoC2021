decoder = '####....##..####..##.#.#.##..##...##.####....####.##..#.######.#####..##.#..#..#..###.#..###........#...' \
          '########...#.#........#...####...#...##...####..###..#..#..##..#####...##.######...###.##.##..#...##....#' \
          '.#...#.######.##.##.#..#.#..#..####.#####....#.##.####..#.##..#...##.#.#####.#..##......###.#..###.##.#.#' \
          '..##...###..#..#..#.###...##.#....#.....##...##..#.##.#.#.....###..#.#...####..#..##.####...###...##...##' \
          '#..#....####..####..#.###.###.##.#.#.#.###.##.#.#.#..#.#...##...#.#.##..#..###.##..##.###.##.'

# decoder = '..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##'\
#             '#..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###'\
#             '.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#.'\
#             '.#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#.....'\
#             '.#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#..'\
#             '...####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.....'\
#             '..##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#'

f = open("input.txt")
dat = [i.strip() for i in f.readlines()]

def printf(f,min_x,min_y,max_x,max_y):
    for y in range(min_y,max_y):
        for x in range(min_x,max_x):
            print(f[(x,y)],end='')
        print("")

from collections import defaultdict
def zero():
    return '0'

def one():
    return '1'

def calc_score(f,min_x,min_y,max_x,max_y):
    count = 0
    for y in range(min_y,max_y):
        for x in range(min_x,max_x):
            count += int(f[(x,y)])
    return count

field = defaultdict(zero)

min_x = 1000000
min_y = 1000000
max_x = -1000000
max_y = -1000000
for y,s in enumerate(dat):
    for x,c in enumerate(s):
        if c == "#":
            field[(x,y)] = "1"

            max_y = max(y,max_y)
            max_x = max(x,max_x)
            min_y = min(y,min_y)
            min_x = min(x,min_x)

calc_min_x = min_x
calc_min_y = min_y
calc_max_x = max_x + 1
calc_max_y = max_y + 1

for i in range(50):
    if i%2 == 1:
        new_field = defaultdict(zero)
    else:
        new_field = defaultdict(one)

    for y in range(calc_min_y - 1,calc_max_y + 1):
        for x in range(calc_min_x - 1, calc_max_x + 1):
            arr = [field[(x-1,y-1)],field[(x,y-1)],field[(x+1,y-1)],field[(x-1,y)],field[(x,y)],field[(x+1,y)],
                    field[(x-1,y+1)],field[(x,y+1)],field[(x+1,y+1)]]
            if decoder[int(''.join(arr),2)] == "#":
                new_field[(x,y)] = '1'
            else:
                new_field[(x,y)] = '0'

    calc_min_x -= 2
    calc_min_y -= 2
    calc_max_x += 2
    calc_max_y += 2
    field = new_field
    # printf(field,calc_min_x,calc_min_y,calc_max_x,calc_max_y)
    if i == 1:
        print("1:",calc_score(field,calc_min_x,calc_min_y,calc_max_x,calc_max_y))

print("2:",calc_score(field,calc_min_x,calc_min_y,calc_max_x,calc_max_y))


