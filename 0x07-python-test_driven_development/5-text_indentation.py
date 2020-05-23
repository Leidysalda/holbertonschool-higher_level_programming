#!/usr/bin/python


def text_indentation(text):
    """
    function that prints a text with 2 new lines after
    each of these characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError('text must be a string')
    else:
        for l in range(len(text)):
            if text[l] == '.' or text[l] == '?' or text[l] == ':':
                print(text[l], end='\n')
            elif text[l] == ' ' and (text[l - 1] == '.' or
                                     text[l - 1] == '?' or text[l - 1] == ':'):
                continue
            else:
                print(text[l], end='')
