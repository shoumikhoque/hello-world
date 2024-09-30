def max_units(boxTypes, truckSize):
    boxTypes = sorted(boxTypes, key=lambda x: x[1],reverse=True)
    ans=0
    for box in boxTypes:
        if truckSize==0:
            return ans
        if box[0]> truckSize:
            ans += box[1] * truckSize
            return ans
        else:
            ans += box[1] * box[0]
            truckSize -= box[0]
    return  ans



if __name__ == '__main__':
    boxTypes = [[5,10],[2,5],[4,7],[3,9]]
    truckSize = 10
    print(max_units(boxTypes,truckSize))