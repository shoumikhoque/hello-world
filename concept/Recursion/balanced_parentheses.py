from concept.Stack.Stack import Stack
def is_balanced_recursive(s:str,index:int,prev:str):
    if index==len(s):
        return True
    if s[index]==')' and prev=='(':
        return is_balanced_recursive(s,index+1,'(')
    else:
        return is_balanced_recursive(s, index + 1, s[index])

def is_balaced_using_stack(s):
    stack=Stack()
    for i in s:
        if i=='(':
            stack.push(i)
        else:
            if stack.is_empty():
                stack.push(i)
            elif stack.peek()=='(':
                stack.pop()
            else:
                stack.push(i)
    return  stack.is_empty()


if __name__ == '__main__':
    s='(()))'
    print(is_balanced_recursive(s,1,s[0]))