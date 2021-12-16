f = open("input.txt")
dat = f.read().strip()

# dat = 'A0016C880162017C3686B18A3D4780'
full_str = bin(int(dat, 16))[2:]

if len(full_str) < len(dat)*4:
    full_str = '0'*(len(dat)*4 - len(full_str)) + full_str


def get_value(s):
    ptr = 0
    v = ''
    while True:
        v += s[ptr + 1:ptr + 5]
        if s[ptr] == '0':
            ptr += 5
            break
        ptr += 5

    return int(v, 2), ptr


def get_packet_val(vals, t_id):
    if t_id == 0:
        return sum(vals)
    if t_id == 1:
        prod = 1
        for x in vals:
            prod *= x
        return prod
    if t_id == 2:
        return min(vals)
    if t_id == 3:
        return max(vals)
    if t_id == 5:
        return 1 if vals[0] > vals[1] else 0
    if t_id == 6:
        return 1 if vals[0] < vals[1] else 0
    if t_id == 7:
        return 1 if vals[0] == vals[1] else 0


def unpack(binstr):
    ptr = 0
    version_count = 0

    while ptr < len(binstr) and '1' in binstr[ptr:]:
        version = int(binstr[ptr:ptr + 3], 2)
        version_count += version
        t_id = int(binstr[ptr + 3:ptr + 6], 2)
        if t_id == 4:
            vals = []
            rt_vals, add_ptr = get_value(binstr[ptr+6:])
            vals.append(rt_vals)
            ptr += add_ptr + 6
            return vals, ptr, version_count
        elif t_id != 4:
            len_type_id = int(binstr[ptr+6])
            if len_type_id == 0:
                sub_packet_len = int(binstr[ptr+7:ptr+22], 2)
                ptr += 22
                vals = []
                og_ptr = ptr
                while '1' in binstr[ptr:og_ptr + sub_packet_len]:
                    rt_vals, add_ptr, add_version_count = unpack(binstr[ptr:])
                    vals += rt_vals
                    ptr += add_ptr
                    version_count += add_version_count
                return [get_packet_val(vals, t_id)], ptr, version_count

            else:
                sub_packet_count = int(binstr[ptr+7:ptr+18], 2)
                ptr += 18
                vals = []

                for i in range(sub_packet_count):
                    rt_vals, add_ptr, add_version_count = unpack(binstr[ptr:])
                    vals += rt_vals
                    ptr += add_ptr
                    version_count += add_version_count
                return [get_packet_val(vals, t_id)], ptr, version_count


val, _, vers = unpack(full_str)
print("1:",vers)
print("2:",val[0])
