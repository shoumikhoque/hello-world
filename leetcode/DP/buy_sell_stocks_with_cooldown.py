def solve(prices):
    dp={}
    def calc(day,buying):
        if day>=len(prices):
            return 0
        if (day,buying) in dp:
            return dp[(day,buying)]
        cooldown=calc(day+1,buying)
        if buying:
            buy=calc(day+1,not buying)-prices[day]
            dp[(day,buying)]=max(buy,cooldown)
        else:
            sell=calc(day+2,not buying)+prices[day]
            dp[(day,buying)]=max(sell,cooldown)
        return dp[(day,buying)]
    return calc(0,True)


if __name__ == '__main__':
    prices=[1, 2, 3, 0, 2]
    print(solve(prices))