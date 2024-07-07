def longest_palindromic_subsequence_recursive(dp, s, start, end):
    if start>end:
        return 0
    if start==end:
        return 1
    if dp[start][end]==0:
        if s[start]==s[end]:
            dp[start][end]=2+longest_palindromic_subsequence_recursive(dp,s,start+1,end-1)
        else:
            c1=longest_palindromic_subsequence_recursive(dp,s,start+1,end)
            c2=longest_palindromic_subsequence_recursive(dp,s,start,end-1)
            dp[start][end]=max(c1,c2)
    return dp[start][end]


def longest_palindromic_subsequence(s):

    dp = [[0]*len(s)]*len(s)

    return longest_palindromic_subsequence_recursive(dp, s, 0, len(s) - 1)


# Driver code to test the above function
if __name__ == '__main__':
    # print(longest_palindromic_subsequence("cddpd"))
    print(longest_palindromic_subsequence("abcbca"))
    # print(longest_palindromic_subsequence("cddpd"))
    # print(longest_palindromic_subsequence("pqr"))