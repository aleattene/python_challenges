

def sum_missing_numbers(values_lst):
    return sum([x for x in range(min(values_lst), max(values_lst) + 1)]) - sum(values_lst)


