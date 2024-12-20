# The Hashtag Generator
# https://www.codewars.com/kata/52449b062fb80683ec000024

def generate_hashtag(s):
    return answer if s and len(answer := '#' + ''.join(w.title() for w in s.split())) <= 140 else False
