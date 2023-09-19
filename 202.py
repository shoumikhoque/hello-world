def findSumOfSqOfDigits(n):
    temp=0
    while n !=0:
        temp=temp+(n%10)*(n%10)
        n=n/10
    return temp

def isHappy( n: int) -> bool:
    seen = set()
    while n not in seen:
        seen.add(n)
        n = sum([int(x) ** 2 for x in str(n)])
    return n == 1


if __name__ == '__main__':
    print("Hello World!")
    isHappy( 1)