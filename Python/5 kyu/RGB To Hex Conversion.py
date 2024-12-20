# RGB To Hex Conversion
# https://www.codewars.com/kata/513e08acc600c94f01000001

def rgb(r, g, b):
    scope = lambda x: min(255, max(0, x))
    return f"{scope(r):02X}{scope(g):02X}{scope(b):02X}"
