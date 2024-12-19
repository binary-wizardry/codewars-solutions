# Does my number look big in this?
# https://www.codewars.com/kata/5287e858c6b5a9678200083c

def narcissistic( value ):
    return sum(int(n) ** len(str(value)) for n in str(value)) == value
