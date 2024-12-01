def is_palindrome(s):
    for i in  range(len(s)):
        if s[i]!=s[len(s)-1-i]:
            return 'NO'
    return 'YES'


if __name__ == '__main__':
    s=input()
    print(is_palindrome(s))