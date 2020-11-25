def fib():
    x, y = 0, 1

    yield x
    yield y
    counter = 2

    while True:
        x, y = y, x + y
        yield y
        counter += 1


if __name__ == '__main__':
    fib_numbers = fib()
    for i in range(10):
        print(next(fib_numbers))

    for i in range(100):
        print(next(fib_numbers))

    print(next(fib_numbers))

    #for i in fib_numbers:
        #print(i)

