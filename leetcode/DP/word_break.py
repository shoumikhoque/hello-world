def solve(s, words):
    def calc(left, right, pos):
        if pos >= len(words):
            return False
        target = s[left:right + 1]
        if target == '' or target == words[pos]:
            return True
        if len(target) < len(words[pos]):
            return False
        ans = calc(left, right, pos + 1)
        if words[pos] == target[:len(words[pos])]:
            ans = ans or calc(len(words[pos]), right, 0)
        return ans
    return calc(0, len(s) - 1, 0)

if __name__ == '__main__':
    target = "leetcode"
    wordDict =  ["leet","code"]
    print(solve(target,wordDict))