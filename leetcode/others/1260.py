from typing import List





def shiftGrid(grid: List[List[int]], k: int) -> List[List[int]]:
    for i in range(k):
        grid=shiftGridOnce(grid)

def shiftGridOnce(grid):
    n=len(grid)
    ans=[0]*n
    for i in range(n):


    return grid

if __name__ == '__main__':
    print("Hello World!")
    shiftGrid([[1, 2, 3], [4, 5, 6], [7, 8, 9]],1)
# Input: grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], k = 1