# Unique In Order
# https://www.codewars.com/kata/54e6533c92449cc251001667

from itertools import groupby

def unique_in_order(sequence):
    return [k for k, _ in groupby(sequence)]
