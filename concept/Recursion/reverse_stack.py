from concept.Stack.Stack import Stack


def insert_at_bottom(st, item):
    if st.is_empty():
        st.push(item)
    else:
        temp=st.pop()
        insert_at_bottom(st,item)
        st.push(temp)

def reverse_stack(st):
    if not st.is_empty():
        temp=st.pop()
        reverse_stack(st)
        insert_at_bottom(st,temp)



if __name__ == '__main__':
    st=Stack()
    st.push(0)
    st.push(1)
    st.push(2)
    st.push(3)
    print(st)
    rev_stack=reverse_stack(st)
    print(st)