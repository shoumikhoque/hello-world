def can_be_square(matchsticks):
    if len(matchsticks)<4:
        return False
    matchsticks_sum=sum(matchsticks)
    sides=[0]*4
    length=matchsticks_sum//4
    if matchsticks_sum%4!=0:
        return False
    matchsticks.sort(reverse=True)
    if matchsticks[0]>matchsticks_sum/4:
        return False
    def backtrack(i):
        if i==len(matchsticks):
            return True
        for j in range(4):
            if sides[j]+matchsticks[i]<=length:
                sides[j]+=matchsticks[i]
                if backtrack(i+1):
                    return True
                sides[j]-=matchsticks[i]
            if sides[j]==0:
                break
        return False
    return backtrack(0)

if __name__ == '__main__':
    matchsticks = [2, 1, 1, 2, 2,3,1]
    print(can_be_square(matchsticks))