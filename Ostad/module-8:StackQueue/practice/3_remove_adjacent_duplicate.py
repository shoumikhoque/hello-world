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

def remove_duplicate(s):
    st=Stack()
    for i in s:
        if not st.is_empty() and st.peek()==i:
            st.pop()
        else:
            st.push(i)
    s=''
    if st.is_empty():
        return -1
    while not st.is_empty():
        s=st.pop()+s
    return s
if __name__ == '__main__':
    t=int(input().strip())
    for _ in range(t):
        s = input().strip()
        print(remove_duplicate(s))
