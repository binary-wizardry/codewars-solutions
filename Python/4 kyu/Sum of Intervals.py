# Sum of Intervals
# https://www.codewars.com/kata/52b7ed099cdc285c300001cd

def sum_of_intervals(intervals):
    result, boundary = 0, float('-inf')
    for a, b in sorted(intervals):
        boundary = max(boundary, a)
        if b > boundary:
            result += b - boundary
            boundary = b
    return result
