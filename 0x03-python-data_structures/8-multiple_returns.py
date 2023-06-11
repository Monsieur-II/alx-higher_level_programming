#!/usr/bin/python3

def multiple_returns(sentence):
    """Returns a tuple with the length of a string and its
    first character"""
    str_len = len(sentence)
    char_at_0 = None if str_len == 0 else sentence[0]

    my_tuple = (str_len, char_at_0)
    return my_tuple
