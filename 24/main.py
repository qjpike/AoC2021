# from collections import defaultdict
# from collections import deque
# f = open("input.txt")
# dat = [i.split() for i in f.read().split("\n")]
#
# def get_operand(op, regs):
#     if op.isnumeric():
#         return int(op)
#     else:
#         return int(regs[op])
#
# def run_prog(inp):
#     regs = defaultdict(int)
#     inp = deque(str(inp))
#
#     for i in dat:
#         if i[0] == 'inp':
#             regs[i[1]] = get_operand(inp.popleft(),regs)
#         elif i[0] == 'add':
#             regs[i[1]] = get_operand(i[1],regs) + get_operand(i[2],regs)
#         elif i[0] == 'mul':
#             regs[i[1]] = get_operand(i[1],regs) * get_operand(i[2],regs)
#         elif i[0] == 'div':
#             b = get_operand(i[2], regs)
#             if b != 0:
#                 regs[i[1]] = get_operand(i[1],regs) // b
#             else:
#                 return False
#         elif i[0] == 'mod':
#             a = get_operand(i[1],regs)
#             b = get_operand(i[2],regs)
#             if a<0 or b <= 0:
#                 return False
#             regs[i[1]] = a%b
#         elif i[0] == 'eql':
#             if get_operand(i[1],regs) == get_operand(i[2],regs):
#                 regs[i[1]] = 1
#             else:
#                 regs[i[1]] = 0
#
#     if regs['z'] == 0:
#         return True
#
#
# for i in range(11111111111111,99999999999999):
#     if int(i)%1000000 == 0:
#         print(i)
#         continue
#     elif '0' in str(i):
#         continue
#     else:
#         if run_prog(i):
#             print(i)
#             break

def calc_new_z(prev_z, w, a, b, c):
    x = prev_z %26
    z = prev_z // a
    x -= b
    x = 0 if x == w else 1
    z = (25*x + 1) * z
    y = (w + c)*x
    z += y
    return z


a = [1, 1, 1, 1, 26, 26, 1, 1, 26, 26, 1, 26, 26, 26]
b = [13, 12, 12, 10, -11, -13, 15, 10, -2, -6, 14, 0, -15, -4]
c = [8, 13, 8, 10, 12, 1, 13, 5, 10, 3, 2, 2, 12, 7]

from collections import defaultdict


prevs = defaultdict(list)

for j in range(1,10):
    prevs[calc_new_z(0,j,a[0],b[0],c[0])] = [str(j)]
print(prevs)

for i in range(13):
    news = defaultdict(list)
    for old_z, list in prevs.items():
        for j in range(1,10):
            new_z = calc_new_z(0, j, a[i+1], b[i+1], c[i+1])
            
print(news)