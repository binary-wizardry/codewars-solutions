# Greed is Good
# https://www.codewars.com/kata/5270d0d18625160ada0000e4

from collections import Counter

def score(dice):
    dice = Counter(dice)
    scores_by_triplets = {1: 1000, 6: 600, 5: 500, 4: 400, 3: 300, 2: 200}
    scores_by_singles = {1: 100, 5: 50}
    triplets = [dice[key] // 3 * scores for key, scores in scores_by_triplets.items()]
    singles = [dice[key] % 3 * scores for key, scores in scores_by_singles.items()]
    return sum(triplets + singles)
