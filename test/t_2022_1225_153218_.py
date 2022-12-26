def t1():
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [0]
    print(a)
    print(b)
    print(c)
    c.extend(a)
    c.extend(b)
    print(a)
    print(b)
    print(c)


if __name__ == '__main__':
    t1()
