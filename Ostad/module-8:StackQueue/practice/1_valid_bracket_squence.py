class Stack:
    def __init__(self, items=[]):
        self.items = items

    def get_size(self):
        return len(self.items)

    def is_empty(self):
        return self.get_size() == 0

    def push(self, val):
        self.items.append(val)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[self.get_size() - 1]

    def __str__(self):
        return str(self.items)


def is_valid_parenthesis(s):
    st = Stack()
    openings = ['(', '{', '[']
    closings = [')', '}', ']']
    for i in s:
        if i in closings:
            if st.is_empty() or closings[openings.index(st.pop())] != i:
                return 'Not valid'
    else:
        st.push(i)
    if not st.is_empty():
        return 'Not valid'
    return 'Valid'

if __name__ == '__main__':
    # t = int(input())
    # for _ in range(t):
    #     s = input().strip()
    #     print(is_valid_parenthesis(s))
    print(is_valid_parenthesis('[][(){}{}(()([](({{}}{()}()[])()(())())))()](())[[][{([({}(()()))[]({{[[{}](([]{[](([]{{}}[]){({})}()[[()]{}])}[[]]((()([[]][{(([][({}{}([])({}([{}[{}[()[]{()}[{}'))
