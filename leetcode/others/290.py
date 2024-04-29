def wordPattern( pattern: str, s: str) -> bool:
    map={}
    s=s.split(" ")
    n=len(pattern)
    for i in range(n):
        if pattern[i] not in map:
            map[pattern[i]]=s[i]
        elif pattern[i] in map and map[pattern[i]] != s[i]:
            return False
    return True
if __name__ == '__main__':
    print(wordPattern("abba", "dog cat cat Fish"))