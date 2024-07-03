def longest_common_substr_length(s1:list, s2:list,dp,count):
    """
    Finds a longest common substring length
    :param s1: First string
    :param s2: Second string
    :return: Length of longest common substring
    """
    if len(s1) == 0 or len(s2) == 0:
        return 0
    key = s1 + ',' + s2
    if key in dp:
        return dp[key]
    if s1[0] == s2[0]:
        count = 1 + longest_common_substr_length(s1[1:], s2[1:], dp,count+1)
    else:
        dp[key] = max(longest_common_substr_length(s1[1:], s2, dp,0), longest_common_substr_length(s1, s2[1:], dp,0))
    return dp[key]

    # Write your code here!
    pass
if __name__ == '__main__':
    s1 = "www.educative.io/explore"
    s2 = "educative.io/edpresso"
    dp=dict()
    print(longest_common_substr_length(s1,s2,dp))