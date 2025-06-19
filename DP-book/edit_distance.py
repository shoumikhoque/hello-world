def solve(s1, s2):
    l1 = len(s1)
    l2 = len(s2)

    def calc(i, j):
        if i == l1:
            return l2 - j
        if j == l2:
            return l1 - i
        if s1[i] == s2[j]:
            return calc(i + 1, j + 1)
        return 1 + min(calc(i + 1, j), calc(i + 1, j + 1), calc(i, j + 1))
    return calc(0, 0)


if __name__ == '__main__':
    s1 = 'saturday'
    s2 = 'sunday'
    print(solve(s1, s2))
