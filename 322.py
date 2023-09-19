class Solution(object):
    def coinChange(self, coins, amount):
        sorted_coins=sorted(coins,reverse=True)
        dp={0:0}
        return self.calculate(coins,amount,dp)
    def calculate(self,coins, amount, dp):
        if amount<0:
            return -1
        if amount in dp:
            return dp[amount]
        for i in coins:
            if amount>=i:
                if amount in dp:
                    return dp[amount]
                else:
                    temp=self.calculate(coins,amount-i,dp)
                    if temp != -1:
                        dp[amount]=temp+1
        if amount in dp:
            return dp[amount]
        else:
            return -1

if __name__ == '__main__':
    coins = [1, 2, 5]
    sorted_coins = sorted(coins, reverse=True)
    amount = 11
    print(Solution.coinChange(,sorted_coins, amount))



