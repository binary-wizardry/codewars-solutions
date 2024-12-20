# Pete, the baker
# https://www.codewars.com/kata/525c65e51bf619685c000059

def cakes(recipe, available):
    return min(available.get(ingredient, 0) // value for ingredient, value in recipe.items())
