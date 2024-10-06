def restore_ip_address(s):
    if len(s)>12:
        return []
    res=[]
    def backtrack(i, dots,current_ip):
        if dots==4 and i==len(s):
            res.append(current_ip[:-1])
            return
        if dots>3:
            return
        for j in range(i,min(i+3,len(s))):
            if int(s[i:j+1])<256 and (i==j or s[i]!='0'):
                backtrack(j+1,dots+1,current_ip+s[i:j+1]+'.')
    backtrack(0,0,'')
    return res

if __name__ == '__main__':
    s = "25525511135"
    print(restore_ip_address(s))