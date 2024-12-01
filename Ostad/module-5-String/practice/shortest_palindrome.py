# TODO incomplete
def longest_palindrome_subsequence(dp,s:str,start:int,end:int):
    if start > end:
        return False
    if start==end:
        dp[str(start)+','+str(end)]=True
        return True
    if str(start)+','+str(end) in dp:
        return dp[str(start)+','+str(end)]
    else:
        if s[start]==s[end]:
            dp[str(start)+','+str(end)]=True and longest_palindrome_subsequence(dp,s,start+1,end-1)
        else:
            dp[str(start) + ',' + str(end)] = False
            dp[str(start+1)+','+str(end)]=longest_palindrome_subsequence(dp, s, start + 1, end)
            dp[str(start+1)+','+str(end-1)]=longest_palindrome_subsequence(dp, s, start,end - 1)

        return dp[str(start)+','+str(end)]

if __name__ == '__main__':

    s="abcbaa"
    dp = dict()
    longest_palindrome_subsequence(dp, s, 0, len(s) - 1)
    print(dp)