def is_funny_string(s):
    for i, c in enumerate(s):
        if i%2==0 and c>='A' and c<='Z':
            return 'No'
        elif i%2==1 and c>='a' and c<='z':
            return 'No'
    return 'Yes'


if __name__ == '__main__':
    s=input()
    print(is_funny_string(s))