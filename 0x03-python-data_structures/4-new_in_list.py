#!/usr/bin/python3

def new_in_list(my_list, idx, element):
   new_list = [element if i == idx + 1 else i for i in my_list]
   return new_list
