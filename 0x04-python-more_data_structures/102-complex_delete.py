#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_list = list(a_dictionary.items())
    for v in new_list:
        if value == v[1]:
            del a_dictionary[v[0]]
    return (a_dictionary)
