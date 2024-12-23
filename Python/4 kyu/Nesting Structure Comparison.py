# Nesting Structure Comparison
# https://www.codewars.com/kata/520446778469526ec0000001

def same_structure_as(original,other):
    if isinstance(original, list) and isinstance(other, list) and len(original) == len(other):
        for item, other_item in zip(original, other):
            if not same_structure_as(item, other_item):
                return False
        else:
            return True
    else:
        return not isinstance(original, list) and not isinstance(other, list)
