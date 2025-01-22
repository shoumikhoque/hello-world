from decimal import Decimal

def egg_drop(eggs, floors,dp):
    if eggs<=0:
        return 0
    if eggs==1:
        return floors
    if floors==0 or floors==1:
        return floors
    if dp[eggs][floors] != Decimal("Infinity"):
        return dp[eggs][floors]
        # Consider all droppings from 1st floor to kth floor and
        # return the minimum of these values plus 1.
    for i in range(1, floors + 1):
        dp[eggs][floors]=min(dp[eggs][floors],
                             1 + max(egg_drop(eggs - 1, i - 1, dp),egg_drop(eggs, floors - i, dp)))

    return dp[eggs][floors]
def egg_drop_table(eggs,floors):
    if eggs<=0:
        return 0
    if eggs==1:
        return floors
    if floors==0 or floors==1:
        return 0
    dp=[[Decimal("Infinity") for i in range(floors+1)] for i in range(eggs+1)]
    for i in range(1,eggs+1):
        dp[i][0]=0
        dp[i][1]=1
    for j in range(1,floors+1):
        dp[1][j]=j
    for i in range(2,eggs+1):
        for j in range(2,floors+1):
            for x in range(1,j+1):
                breaks=dp[i-1][x-1]
                not_breaks=dp[i][j-x]
                dp[i][j]=min(dp[i][j],1+max(breaks,not_breaks))
    return dp[eggs][floors]


if __name__ == '__main__':
    eggs,floors=5,100
    dp = [[Decimal("Infinity") for i in range(floors + 1)] for i in range(eggs + 1)]
    print(egg_drop_table(eggs, floors))