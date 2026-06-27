def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    char_count = {}

    for char in s: 
        char_count[char] = char_count.get(char, 0) + 1

    for char in t:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] < 0:
            return False

    return all(count == 0 for count in char_count.values())


if __name__ == "__main__":
    # Test cases
    print(is_anagram("anagram", "nagaram"))  # True
    print(is_anagram("rat", "car"))          # False
    print(is_anagram("listen", "silent"))    # True
    print(is_anagram("hello", "billion"))    # False

