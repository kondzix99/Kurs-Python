import itertools as it

# def get_factors(x):
#     ret_list = []
#     for i in range(1, x):
#         if x % i == 0:
#             ret_list.append(i)
#     return ret_list
#
# candidate_list = [i for i in range(1,10000)]
#
# filtered_list = list(it.filterfalse(lambda x : x != sum(get_factors(x)), candidate_list))
#
# for p in filtered_list:
#     print(p, get_factors(p))


def check_if_has_dividers(x):
    for i in range(2, x):
        if x % i == 0:
            return True
    else:
        return False

print(check_if_has_dividers(7))