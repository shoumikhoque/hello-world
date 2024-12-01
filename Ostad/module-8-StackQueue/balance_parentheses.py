class Stack:
    def __init__(self,items=[]):
        self.items=items
    def get_size(self):
        return len(self.items)
    def is_empty(self):
        return self.get_size()==0
    def push(self,val):
        self.items.append(val)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[self.get_size()-1]
    def __str__(self):
        return str(self.items)
def balance_parentheses(s):
    st = Stack()
    openings = ['(', '{', '[']
    closings = [')', '}', ']']
    for i in range(len(s)):
        if s[i] in closings:
            if not st.is_empty() and closings[openings.index(st.pop())] != s[i]:
                return False
        else:
            st.push(s[i])
    if not st.is_empty():
        return False
    return True

if __name__ == '__main__':
    s='[{(})]'
    print(balance_parentheses(s))