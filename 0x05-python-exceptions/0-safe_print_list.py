#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    acum = 0
    try:
        for i in my_list[0:x]:
            acum += 1
            print('{}'.format(i), end='')
        print()
        return (acum)
    except ValueError:
        print('Error')
