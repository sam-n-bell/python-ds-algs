

def is_palindrome(string: str) -> bool:
    if len(string) < 2:
        return False
        
    left = 0
    right = len(string) - 1
    while left <= right:
        if string[left] != string[right]:
            # left and right characters don't match
            return False
        left += 1
        right -= 1

    # got all the way through
    return True

strings = ['hannah', 'racecar', 'alex', 'b', '', 'none']
for string in strings:
    print(is_palindrome(string))
