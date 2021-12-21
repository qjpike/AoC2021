# the plan:
# 1. put all the scanners into a queue ('unknown list')
# 2. take the first scanner out of the queue. Add the scanner into the 'known list'. It's beacons become the field
# 3. for all of the scanners in the list try:
#     3.a all permutations of the beacons, adjusted to match each beacon known in the field
#     3.b if any of the adjusted permutations of the beacons of an individual scanner match 12 or more
#         of the known beacons in the field:
#         3.b.1 set that permutation as the final location of the beacons
#         3.b.2 add those beacons to the field
#         3.b.3 calculate the location of the scanner
#         3.b.4 move that scanner from the unknown list into the known list
#     3.c if they dont match, add that scanner back to the list
# 4. (answer for part 1) the number of scanners is the number of known beacons in the field
# 5. (answer for part 2) calculate the distance between all of the scanners, find the max


from collections import deque

class Scanner():
    def __init__(self,name,vals):
        self.name = name
        self.og_locs = vals
        self.final_locs = None
        self.scanner_loc = None
        self.perm_idx = None
        self.all_perms = []
        self.all_perms.append([(x, y, z) for x,y,z in self.og_locs])
        self.all_perms.append([(x, z, -y) for x,y,z in self.og_locs])
        self.all_perms.append([(x, -y, -z) for x, y, z in self.og_locs])
        self.all_perms.append([(x, -z, y) for x, y, z in self.og_locs])
        self.all_perms.append([(-x, -y, z) for x, y, z in self.og_locs])
        self.all_perms.append([(-x, z, y) for x, y, z in self.og_locs])
        self.all_perms.append([(-x, y, -z) for x, y, z in self.og_locs])
        self.all_perms.append([(-x, -z, -y) for x, y, z in self.og_locs])
        self.all_perms.append([(y, z, x) for x, y, z in self.og_locs])
        self.all_perms.append([(y, x, -z) for x, y, z in self.og_locs])
        self.all_perms.append([(y, -z, -x) for x, y, z in self.og_locs])
        self.all_perms.append([(y, -x, z) for x, y, z in self.og_locs])
        self.all_perms.append([(-y, -z, x) for x, y, z in self.og_locs])
        self.all_perms.append([(-y, x, z) for x, y, z in self.og_locs])
        self.all_perms.append([(-y, z, -x) for x, y, z in self.og_locs])
        self.all_perms.append([(-y, -x, -z) for x, y, z in self.og_locs])
        self.all_perms.append([(z, x, y) for x, y, z in self.og_locs])
        self.all_perms.append([(z, y, -x) for x, y, z in self.og_locs])
        self.all_perms.append([(z, -x, -y) for x, y, z in self.og_locs])
        self.all_perms.append([(z, -y, x) for x, y, z in self.og_locs])
        self.all_perms.append([(-z, -x, y) for x, y, z in self.og_locs])
        self.all_perms.append([(-z, y, x) for x, y, z in self.og_locs])
        self.all_perms.append([(-z, x, -y) for x, y, z in self.og_locs])
        self.all_perms.append([(-z, -y, -x) for x, y, z in self.og_locs])

    def __str__(self):
        return str(self.name) + ": " + str(self.og_locs)

    def calc_scanner_loc(self):
        perm_x, perm_y, perm_z = self.all_perms[self.perm_idx][0]
        final_x, final_y, final_z = self.final_locs[0]
        self.scanner_loc = (final_x - perm_x,final_y - perm_y, final_z - perm_z)


def parse_input():
    f = open("input.txt")
    dat = [i.strip() for i in f.readlines()]

    scanners = deque()
    cur_scanner = []
    name = -1
    for i in dat:
        if i.startswith('---'):
            name = int(i.split()[2])
        elif i == "":
            scanners.append(Scanner(name, cur_scanner))
            cur_scanner = []
            name = -1
        else:
            cur_scanner.append((int(i.split(",")[0]),int(i.split(",")[1]),int(i.split(",")[2])))

    return scanners


# step 1
unknown_scanners = parse_input()
# step 2
known_scanners = [unknown_scanners.popleft()]
known_beacons = set(known_scanners[0].og_locs)
known_scanners[0].final_locs = known_scanners[0].og_locs
known_scanners[0].scanner_loc = (0,0,0)


def fit_scanner(cur_scanner, known_beacons):
    # step 3a
    for anchor_x, anchor_y, anchor_z in list(known_beacons):
        for perm, perm_list in enumerate(cur_scanner.all_perms):
            for perm_x, perm_y, perm_z in perm_list:
                delta_x = anchor_x - perm_x
                delta_y = anchor_y - perm_y
                delta_z = anchor_z - perm_z
                beacons_permed = [(x + delta_x, y + delta_y, z + delta_z) for x, y, z in perm_list]
                # step 3b
                if len(known_beacons & set(beacons_permed)) >= 12:
                    # print("Found:",cur_scanner.name)
                    cur_scanner.perm_idx = perm
                    cur_scanner.final_locs = beacons_permed # 3.b.1
                    known_beacons |= set(beacons_permed) # 3.b.2
                    cur_scanner.calc_scanner_loc() # 3.b.3
                    # print(cur_scanner.name,":",cur_scanner.scanner_loc)
                    return True
    return False

# step 3
while unknown_scanners:
    cur_scanner = unknown_scanners.popleft()
    if not fit_scanner(cur_scanner, known_beacons):
        unknown_scanners.append(cur_scanner)
    else:
        known_scanners.append(cur_scanner) # 3.c


print("1:",len(known_beacons)) # 4

# step 5
max_d = 0
for s1 in known_scanners:
      for s2 in known_scanners:
          max_d = max(abs(s1.scanner_loc[0] - s2.scanner_loc[0]) + abs(s1.scanner_loc[1] - s2.scanner_loc[1]) + \
                    abs(s1.scanner_loc[2] - s2.scanner_loc[2]), max_d)

print("2:",max_d)