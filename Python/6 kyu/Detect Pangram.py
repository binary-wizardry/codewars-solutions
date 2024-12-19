# Detect Pangram
# https://www.codewars.com/kata/545cedaa9943f7fe7b000048

from string import ascii_lowercase

def is_pangram(st):
    return set(s for s in st.lower() if s.isalpha()) == set(ascii_lowercase)
