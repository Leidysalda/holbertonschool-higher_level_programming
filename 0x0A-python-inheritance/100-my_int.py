#!/usr/bin/python3


class MyInt(int):
    """Class MyInt"""
    def __eq__(self, num):
        """Method __eq__ equal"""
        return(int(self) != int(num))

    def __ne__(self, num):
        """Method __ne__ diferent"""
        return(int(self) == int(num))
