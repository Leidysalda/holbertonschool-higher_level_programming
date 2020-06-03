#!/usr/bin/python3


class MyList(list):
    """Class MyList that inherits from list"""

    def print_sorted(self):
        """
        Print list sorted
        """
        new_list = self[:]
        return(sorted(new_list))
