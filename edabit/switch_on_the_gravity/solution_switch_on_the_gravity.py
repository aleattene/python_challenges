

def switch_gravity_on(lst):
    for i in range(len(lst)-2, -1, -1):
        for j in range(len(lst[i]) -1, -1, -1):
            if lst[i][j] == '#':
                lst[i][j] = "-"
                k = len(lst) - 1
                while True:
                    if k < 0:
                        break
                    if lst[k][j] != "#":
                        lst[k][j] = "#"
                        break
                    k -= 1
    return lst

