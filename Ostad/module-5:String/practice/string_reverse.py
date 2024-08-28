def reverse_string(s):
    ans=''
    for i in range(len(s)):
        ans+=s[len(s)-1-i]
    return ans


if __name__ == '__main__':
    s=input()
    print(reverse_string(s))