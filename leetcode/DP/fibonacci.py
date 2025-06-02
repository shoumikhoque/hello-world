import tracemalloc
def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)
def fib_table(n):
    if n == 0 or n == 1:
        return n
    dp = [1,1]+[0] * (n - 1)
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


if __name__ == '__main__':
    tracemalloc.start()
 # in bytes
    print(fib_table(100000))
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Memory used: {(peak - current) :.2f} B")
