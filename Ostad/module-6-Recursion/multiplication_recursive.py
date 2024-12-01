def multiplication_recursive(a, b):
    if b>a:
        multiplication_recursive(b,a)
    if b==0:
        return 0
    return a+ multiplication_recursive(a,b-1)


if __name__ == '__main__':
    a=1000
    b=997
    print(multiplication_recursive(a,b))