from typing import List


def calculateWaysToClimb(n: int, fib: List[int]) -> int:
    if fib[n] != 0:
        return fib[n]
    else:
        fib[n] = calculateWaysToClimb(n - 1, fib) + calculateWaysToClimb(n - 2, fib)
        return fib[n]


def climbStairs( n: int) -> int:
    fib = [0] * (n + 1)
    fib[0] = 1
    fib[1] = 1

    return calculateWaysToClimb(n, fib)



if __name__ == '__main__':
    # print(insertionSort([5,2,4,6,1,3]))