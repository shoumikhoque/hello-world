def solve(days, costs):
    costs={
        1:costs[0],
        7:costs[1],
        30:costs[2]
    }
    dp={}
    def calc(index):
        if index>=len(days):
            return 0
        if days[index]
    calc(0)



if __name__ == '__main__':
    days = [1, 4, 6, 7, 8, 20]
    costs = [2, 7, 15]
    print(solve(days,costs))