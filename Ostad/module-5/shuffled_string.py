def shuffle_string(s, indices):
    ans = [''] * len(indices)
    for i in range(len(s)):
        ans[indices[i]] = s[i]
    s = ''
    for i in ans:
        s += i
    return s


if __name__ == '__main__':
    s = 'mamacode'
    indices = [4, 5, 6, 7, 0, 1, 2, 3]
    print(shuffle_string(s,indices))