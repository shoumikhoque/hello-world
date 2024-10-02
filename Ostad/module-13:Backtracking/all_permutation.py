def all_permutaions(pat,ans='',result=[]):
    if pat=='':
        result.append(ans)
        return
    for i in range(len(pat)):
        all_permutaions(pat[:i] + pat[i + 1:],ans+pat[i],result)
    return result

if __name__ == '__main__':
    pat='abcd'
    print(all_permutaions(pat))