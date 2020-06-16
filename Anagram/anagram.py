from collections import Counter


def are_anagrams(string1: str, string2: str) -> bool:
    if not string1 or not string2 or len(string1) != len(string2):
        return False

    return Counter(string1.lower()) == Counter(string2.lower())
