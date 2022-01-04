from collections import deque

f = open("input.txt")
dat = [i.split(",") for i in f.read().split("\n")]
f.close()

def get_bounds(inp):
    x, y, z = inp
    x_min = int(x[x.index("=") + 1:x.index(".")])
    x_max = int(x.split(".")[-1])
    y_min = int(y[2:y.index(".")])
    y_max = int(y.split(".")[-1])
    z_min = int(z[2:z.index(".")])
    z_max = int(z.split(".")[-1])

    return x_min, x_max, y_min, y_max, z_min, z_max


class Cube:
    def __init__(self, x_min, x_max, y_min, y_max, z_min, z_max, onoff):
        self.x_min = x_min
        self.y_min = y_min
        self.z_min = z_min
        self.x_max = x_max
        self.y_max = y_max
        self.z_max = z_max
        self.size = (x_max + 1 - x_min) * (y_max + 1 - y_min) * (z_max + 1 - z_min)

        self.state = onoff

    def inside(self, other):
        return self.x_min >= other.x_min and self.x_max <= other.x_max and \
                self.y_min >= other.y_min and self.y_max <= other.y_max and \
                self.z_min >= other.z_min and self.z_max <= other.z_max

    def slice_x(self, plane, m):
        if m:
            l = Cube(self.x_min, plane - 1, self.y_min, self.y_max, self.z_min, self.z_max, self.state)
            r = Cube(plane, self.x_max, self.y_min, self.y_max, self.z_min, self.z_max, self.state)
        else:
            l = Cube(self.x_min, plane, self.y_min, self.y_max, self.z_min, self.z_max, self.state)
            r = Cube(plane + 1, self.x_max, self.y_min, self.y_max, self.z_min, self.z_max, self.state)
        return l,r

    def slice_y(self, plane, m):
        if m:
            l = Cube(self.x_min, self.x_max, self.y_min, plane - 1, self.z_min, self.z_max, self.state)
            r = Cube(self.x_min, self.x_max, plane, self.y_max, self.z_min, self.z_max, self.state)
        else:
            l = Cube(self.x_min, self.x_max, self.y_min, plane, self.z_min, self.z_max, self.state)
            r = Cube(self.x_min, self.x_max, plane + 1, self.y_max, self.z_min, self.z_max, self.state)
        return l,r

    def slice_z(self, plane, m):
        if m:
            l = Cube(self.x_min, self.x_max, self.y_min, self.y_max, self.z_min, plane - 1, self.state)
            r = Cube(self.x_min, self.x_max, self.y_min, self.y_max, plane, self.z_max, self.state)
        else:
            l = Cube(self.x_min, self.x_max, self.y_min, self.y_max, self.z_min, plane, self.state)
            r = Cube(self.x_min, self.x_max, self.y_min, self.y_max, plane + 1, self.z_max, self.state)
        return l,r

    def set_new_coords(self, other):
        self.x_min = other.x_min
        self.y_min = other.y_min
        self.z_min = other.z_min
        self.x_max = other.x_max
        self.y_max = other.y_max
        self.z_max = other.z_max
        self.size = (self.x_max + 1 - self.x_min) * (self.y_max + 1 - self.y_min) * (self.z_max + 1 - self.z_min)

    def slice(self, other):

        returns = []
        if self.x_min < other.x_min <= self.x_max:
            keep, new_self = self.slice_x(other.x_min, True)
            returns.append(keep)
            self.set_new_coords(new_self)
            if self.inside(other):
                return returns
        if self.x_min <= other.x_max < self.x_max:
            new_self, keep = self.slice_x(other.x_max, False)
            returns.append(keep)
            self.set_new_coords(new_self)
            if self.inside(other):
                return returns
        if self.y_min < other.y_min <= self.y_max:
            keep, new_self = self.slice_y(other.y_min, True)
            returns.append(keep)
            self.set_new_coords(new_self)
            if self.inside(other):
                return returns
        if self.y_min <= other.y_max < self.y_max:
            new_self, keep = self.slice_y(other.y_max, False)
            returns.append(keep)
            self.set_new_coords(new_self)
            if self.inside(other):
                return returns
        if self.z_min < other.z_min <= self.z_max:
            keep, new_self = self.slice_z(other.z_min, True)
            returns.append(keep)
            self.set_new_coords(new_self)
            if self.inside(other):
                return returns
        if self.z_min <= other.z_max < self.z_max:
            new_self, keep = self.slice_z(other.z_max, False)
            returns.append(keep)
            self.set_new_coords(new_self)
            if self.inside(other):
                return returns
        return returns

    def intersects(self,other):
        return other.x_min <= self.x_max and self.x_min <= other.x_max and \
                other.y_min <= self.y_max and self.y_min <= other.y_max and \
                other.z_min <= self.z_max and self.z_min <= other.z_max


cubes = deque()
p1 = True
for i in dat:
    a, b, c, d, e, f = get_bounds(i)
    if abs(a) > 50 and p1:
        count = 0
        for n in cubes:
            count += n.size
        print("Part 1:",count)
        p1 = False
    new = Cube(a, b, c, d, e, f, i[0].split()[0])
    if new.state == 'on':
        cubes.append(new)
    new_cubes = deque()
    for n in cubes:
        if n == new:
            new_cubes.append(new)
        else:
            if n.intersects(new):
                new_cubes.extend(n.slice(new))
            else:
                new_cubes.append(n)

    cubes = new_cubes


count = 0
for n in cubes:
    count += n.size
print("Part 2:", count)
