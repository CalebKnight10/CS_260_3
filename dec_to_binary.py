class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def divideBy2(decNumber):
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2

    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return binString


def main():
    print(divideBy2(42))
    print(divideBy2(27))
    print(divideBy2(110))
    print(divideBy2(147))
    print(divideBy2(1917))
    print(divideBy2(192))
    print(divideBy2(1317))



if __name__ == '__main__':
    main()