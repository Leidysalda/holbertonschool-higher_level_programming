#!/usr/bin/python3

def max_integer(my_list=[]):
   if my_list == '':
      return None
   list_ord = sorted(my_list)
   return (list_ord[-1])
