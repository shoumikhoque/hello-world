def is_palindrome(s:str):
    if len(s)<2 :
        return True
    return s[0]==s[len(s)-1] and is_palindrome(s[1:len(s)-1])

if __name__ == '__main__':
    s='saippuakivikauppias'
    print(is_palindrome(s))