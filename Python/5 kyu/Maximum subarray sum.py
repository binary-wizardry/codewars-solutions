# Maximum subarray sum
# https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c

def max_sequence(arr):
    answer, stack = 0, 0
    for n in arr:
        stack = max(0, stack + n)
        answer = max(answer, stack)
    return answer
