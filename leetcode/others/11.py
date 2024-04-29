def hammingWeight( n: int) -> int:
    ans = 0
    while n > 0:
        if n % 2 == 1:
            ans = ans + 1
        n = int(n / 2)
    return ans

print(hammingWeight(11))
