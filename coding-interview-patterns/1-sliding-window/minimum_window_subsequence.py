from operator import index


def min_window(s, pattern):
    n=len(s)
    m=len(pattern)
    i1,i2=0,0
    min_sub_len=float('inf')
    output=''
    while i1<n:
        if s[i1]==pattern[i2]:
            i2+=1
            if i2==m:
                start,end=i1,i1
                i2-=1
                while i2>=0:
                    if s[start]==pattern[i2]:
                        i2-=1
                    start-=1
                start+=1
                if end -start<min_sub_len:
                    min_sub_len=end-start
                    output=s[start:end+1]
                i1=start
                i2=0
        i1+=1
    return output


if __name__ == '__main__':
    str1 = ["abcdedeaqdweq", "fgrqsqsnodwmxzkzxwqegkndaa", "zxcvnhss", "alpha", "beta"]
    str2 = ["adeq", "kzed", "css", "la", "ab"]

    for i in range(len(str1)):
        print(i + 1, ". \tInput string: (" + str1[i] + ", " + str2[i] + ")", sep="")
        print("\tSubsequence string: ", min_window(str1[i], str2[i]))
        print("-" * 100)