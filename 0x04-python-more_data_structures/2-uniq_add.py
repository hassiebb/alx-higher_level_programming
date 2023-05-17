#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_List = set(my_list)
    new_List = list(new_List)
    result = 0
    for i in range(len(new_List)):
        result = result + new_List[i]
    return result
