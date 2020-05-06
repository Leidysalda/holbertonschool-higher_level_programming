#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
   tuple_c = ()
   tuple_d = (0, 0)

   if len(tuple_a) < 2:
      tuple_a = tuple_a + tuple_d
   if len(tuple_b) < 2:
      tuple_b = tuple_b + tuple_d

   tuple_c = tuple(i + j for i, j in zip(tuple_a[0:2], tuple_b[0:2]))
   return (tuple_c)
