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
if __name__ == '__main__':
    stack=Stack()
    stack.push(0)
    stack.push(1)
    print(str(stack))
