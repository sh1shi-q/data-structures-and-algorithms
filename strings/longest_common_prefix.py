def longest_common_prefix(strs: list) -> str:
    if not strs:
        return ""

    prefix = strs[0]

    for string in strs[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix

if __name__ == "__main__":
    # Test cases
    print(longest_common_prefix(["flower", "flow", "flight"]))  # "fl"
    print(longest_common_prefix(["dog", "racecar", "car"]))     # ""
    print(longest_common_prefix(["interspecies", "interstellar", "interstate"]))  # "inters"
    print(longest_common_prefix(["throne", "throne"]))          # "throne"
    print(longest_common_prefix([]))                             # ""
            