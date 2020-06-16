from collections import Counter

def are_anagrams(string1: str, string2: str) -> bool:

    if not string1 or not string2 or len(string1) != len(string2):
        return False

    return Counter(string1.lower()) == Counter(string2.lower())

pairs = [('bob', 'bbo'), ('race', 'care'), ('sam', 'josh'), ('sam', 'tes'), ('sam', 'Sam'), (None, '')]
for pair in pairs:
    print(f'are {pair[0]} and {pair[1]} anagrams? {are_anagrams(pair[0], pair[1])}')
