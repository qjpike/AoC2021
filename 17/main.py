block_x_min = 153
block_x_max = 199
block_y_min = -114
block_y_max = -75

# block_x_min = 20
# block_x_max = 30
# block_y_min = -10
# block_y_max = -5

block = set()
for y in range(block_y_min, block_y_max+1):
    for x in range(block_x_min, block_x_max + 1):
        block.add((x,y))


def shoot(x_vel,y_vel):
    x = y = 0
    y_max = 0
    while x <= block_x_max and y >= block_y_min:
        x += x_vel
        y += y_vel
        if x_vel > 0:
            x_vel -= 1
        y_vel -= 1
        if y > y_max:
            y_max = y
        if (x,y) in block:
            return True,y_max
    return False,y_max

y_max = 0
hits = 0
for y in range(block_y_min,-block_y_min+1):
    for x in range(0,block_x_max+1):
        hit, cur_y_max = shoot(x,y)
        if hit:
            hits += 1
            if cur_y_max > y_max:
                y_max = cur_y_max


print(y_max) # 21 wrong; 1035 too low
# I had my block_y_max set to -57 instead of -75 for a very long time. dumb.
print(hits) # 255 too low; 1726 too low; 4405 too high; 1771 wrong; 4497 wrong; 4155 wrong;
