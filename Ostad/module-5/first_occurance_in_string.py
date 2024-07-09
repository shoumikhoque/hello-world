def find_first_occurrence_kmp(haystack: str, needle: str) -> int:
    # Time : O(m + n), m = len(needle), n = len(haystack)
    # Space :O(m)

    # Step 1: Create the Longest Prefix Suffix (LPS) array for the pattern
    lps = [0] * len(needle)  # Initialize LPS array to all zeros
    pre = 0  # Length of the previous longest prefix suffix

    # Preprocessing the pattern to create the LPS array
    for i in range(1, len(needle)):
        while pre > 0 and needle[i] != needle[pre]:
            pre = lps[pre - 1]
        if needle[pre] == needle[i]:
            pre += 1
            lps[i] = pre

    # Step 2: Use the LPS array to search the pattern in the text
    n = 0  # Index for needle
    for h in range(len(haystack)):
        while n > 0 and needle[n] != haystack[h]:
            n = lps[n - 1]
        if needle[n] == haystack[h]:
            n += 1
        if n == len(needle):  # All characters in needle matched
            return h - n + 1  # Return the starting index of the first match

    return -1  # If no match is found

def find_first_occurrance_slicing(haystack, needle):
    # Time : O(m * n), m = len(needle), n = len(haystack)
    # Space :O(1)
    if len(needle)>len(haystack):
        return -1
    for i in range(len(haystack)-len(needle)+1):
        if haystack[i:i+len(needle)]==needle:
            return i
    return -1

if __name__ == '__main__':
    haystack = "abcdabcabcdf"
    needle = "abcdf"
    print(find_first_occurrence_kmp(haystack,needle))