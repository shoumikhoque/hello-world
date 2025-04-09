def solve(prices,fee):
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
            sell=calc(day+1,not buying)+prices[day]-fee
            dp[(day,buying)]=max(sell,cooldown)
        return dp[(day,buying)]
    return calc(0,True)
def solve_table(prices,fee):
    if not prices or len(prices)<=1:
        return 0
    profit=0
    buy=-float("inf")
    for i in prices:
        buy=max(buy,i)
        

if __name__ == '__main__':
    prices=[1,3,7,5,10,3]
    fee=3
    print(solve(prices,fee))