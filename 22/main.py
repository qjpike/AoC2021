f = open("input_1.txt")
dat = [i.strip() for i in f.readlines()]
f.close()

def count_cubes(f):
    count = 0
    for i,val in f.items():
        if val:
            count += 1
    return count

from collections import defaultdict
# field = defaultdict(int)
#
# for i in dat:
#     x,y,z = i.split(",")
#     x_min = int(x[x.index("=")+1:x.index(".")])
#     x_max = int(x.split(".")[-1])
#     y_min = int(y[2:y.index(".")])
#     y_max = int(y.split(".")[-1])
#     z_min = int(z[2:z.index(".")])
#     z_max = int(z.split(".")[-1])
#
#     if x.split()[0] == 'on':
#         val = 1
#     else:
#         val = 0
#
#     for z in range(min(z_min,z_max),max(z_min,z_max) + 1):
#         for y in range(min(y_min,y_max),max(y_min,y_max)+1):
#             for x in range(min(x_min,x_max),max(x_min,x_max)+1):
#                 field[(x,y,z)] = val
#
# print(sum(list(field.values())))

f = open("input.txt")
dat = [i.split(",") for i in f.read().split("\n")]

def get_bounds(inp):
    x,y,z = inp
    x_min = int(x[x.index("=")+1:x.index(".")])
    x_max = int(x.split(".")[-1])
    y_min = int(y[2:y.index(".")])
    y_max = int(y.split(".")[-1])
    z_min = int(z[2:z.index(".")])
    z_max = int(z.split(".")[-1])

    return x_min, x_max, y_min, y_max ,z_min, z_max

class Cube:
    def __init__(self,x_min,x_max,y_min,y_max,z_min,z_max,onoff):
        self.x_min = x_min
        self.y_min = y_min
        self.z_min = z_min
        self.x_max = x_max
        self.y_max = y_max
        self.z_max = z_max
        self.size = (x_max + 1 - x_min)*(y_max + 1 - y_min)*(z_max + 1 - z_min)

        self.state = onoff

    def slice_x(self,plane):
        returns = []
        returns.append(Cube(self.x_min,plane - 1, self.y_min, self.y_max, self.z_min, self.z_max, self.state))
        returns.append(Cube(plane,self.x_max,self.y_min,self.y_max,self.z_min,self.z_max, self.state))
        return returns

    def slice_y(self,plane):
        returns = []
        returns.append(Cube(self.x_min, self.x_max, self.y_min, plane-1,self.z_min, self.z_max, self.state))
        returns.append(Cube(self.x_min, self.x_max, plane, self.y_max, self.z_min, self.z_max, self.state))
        return returns

    def slice_z(self,plane):
        returns = []
        returns.append(Cube(self.x_min, self.x_max, self.y_min, self.y_max, self.z_min, plane-1, self.state))
        returns.append(Cube(self.x_min, self.x_max, self.y_min, self.y_max, plane, self.z_max, self.state))
        return returns

    def intersects(self,other):

        if self.x_min < other.x_min <= self.x_max:
            return self.slice_x(other.x_min)
        elif self.x_min <= other.x_max < self.x_max:
            return self.slice_x(other.x_max)
        elif self.y_min < other.y_min <= self.y_max:
            return self.slice_y(other.y_min)
        elif self.y_min <= other.y_max < self.y_max:
            return self.slice_y(other.y_max)
        elif self.z_min < other.z_min <= self.z_max:
            return self.slice_z(other.z_min)
        elif self.z_min <= other.z_max < self.z_max:
            return self.slice_z(other.z_max)
        return None

from collections import deque

cubes = deque()
for i in dat:
    a,b,c,d,e,f = get_bounds(i)
    if i[0].startswith('on'):
        cubes.append(Cube(a,b,c,d,e,f,i[0].split()[0]))
    else:
        cur = Cube(a,b,c,d,e,f,i[0].split()[0])
        comp_cubes = cubes.copy()
        while len(comp_cubes) > 0:
            now = comp_cubes.popleft()
            splits = now.intersects(cur)
            if splits:
                comp_cubes.append(now.intersects(cur))
                cubes.__delitem__(now)
                cubes += splits

for i in cubes:
    print(i.size)

# the plan:
# 1. make Cube object for an input line.
#   1.a if it's 'on' put it in a deque
#   1.b if it's 'off' check for intersections with all the cubes in the deque
#       for every 'on' cube it intersects:
#       1.b.1 remove the 'on' cube from the queue
#       1.b.2 slice the 'on' cube into smaller 'on' cubes for each plane that intersects
#       1.b.3 add all the smaller 'on' cubes back into the queue
# 2. for all remaining 'on' cubes, find and account for intersections
