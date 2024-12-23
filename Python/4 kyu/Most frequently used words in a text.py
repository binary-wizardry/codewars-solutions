# Most frequently used words in a text
# https://www.codewars.com/kata/51e056fe544cf36c410000fb

import re
from collections import Counter

def top_3_words(text):
    text = re.sub(r"\s\'+\s", '', text.lower())
    result = Counter()
    for word in re.finditer(r"[a-z\']+", text):
        result[word.group()] += 1
    return [word for word, count in result.most_common(3)]
