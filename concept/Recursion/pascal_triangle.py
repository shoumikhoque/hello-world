def pascal_triangle(level):
    if level==0:
        return [1]
    else:
        ans=[1]
        prev=pascal_triangle(level-1)
        print(prev)
        for i in range(len(prev)-1):
            ans.append(prev[i]+prev[i+1])
        ans.append(1)
    return ans

if __name__ == '__main__':
    print(pascal_triangle(16))