

def switch_gravity_on(lst):
    for row in range(len(lst)-2, -1, -1):
        for col in range(len(lst[row])-1, -1, -1):
            if lst[row][col] == '#':
                lst[row][col] = "-"
                last_row = len(lst)-1
                while True:
                    if lst[last_row][col] != "#":
                        lst[last_row][col] = "#"
                        break
                    else:
                        last_row -= 1
    return lst

