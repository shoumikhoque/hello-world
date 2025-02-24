


def solve(days, costs):
    costs={
        1:costs[0],
        7:costs[1],
        30:costs[2]
    }
    dp={}

    def next_index_for_30_days(index):
        ans=days[index]
        for i in range(index+1,len(days)):
            if ans>days[index]+29:
                break
            ans=days[i]
        return ans

    def next_index_for_7_days(index):
        ans = days[index]
        for i in range(index+1, len(days)):
            if ans > days[index] + 6:
                break
            ans = days[i]
        return ans
    def calc(index):
        if index>=len(days):
            return 0
        result=costs[0]+calc(index+1)
        result=min( result,costs[1]+calc(next_index_for_7_days(index)),30+ costs[2]+calc(next_index_for_30_days(index)))
        return result
    return calc(0)



if __name__ == '__main__':
    days = [1, 4, 6, 7, 8, 20]
    costs = [2, 7, 15]
    print(solve(days,costs))