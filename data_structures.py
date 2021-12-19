from collections import deque


class HashTable(object):
    def __init__(self, length=4):
        pass
        # self.array = [None] * length

    def hash(self, key):
        pass
        # length = len(self.array)
        # return hash(key) % length

    def add(self, key, value):
        pass
        # add 'is_full' functionality

    def get(self, key):
        pass

    def is_full(self):
        pass

    def double(self):
        pass

    def __setitem__(self, key, value):
        pass

    def __getitem__(self, key):
        pass

    def __contains__(self, item):
        pass

    def __iter__(self):
        pass


class Stack:
    def __str__(self):
        return str(self.items)

    def __len__(self):
        return len(self.items)

    def __init__(self):
        self.items = []

    def __iter__(self):
        self.x = len(self.items) - 1
        return self

    def __next__(self):
        if self.x >= 0:
            y = self.x
            self.x -= 1
            return self.items[y]
        else:
            raise StopIteration

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            print("Empty Stack; Nothing to Pop.")
        else:
            return self.items.pop()

    def peak(self):
        if self.is_empty():
            print("Empty Stack; Nothing to Peak.")
        else:
            print(self.items[-1])

    def is_empty(self):
        return not len(self.items)

    def size(self):
        return len(self.items)

    @staticmethod
    def challenge():
        """Reverses a string using the Stack data structure."""
        challenge_str = "dlroW olleH"       # BO: 1
        my_stack = Stack()                  # BO: 1
        for j in challenge_str:             # BO: n+1+1
            my_stack.push(j)
        rev_str = "".join([x for x in my_stack])
        print(rev_str)


class QueueDeq:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return not self.items

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        self.items.popleft()

    def size(self):
        return len(self.items)

    def front(self):
        return self.items[0]

    def __str__(self):
        return str(self.items)

    def back(self):
        return self.items[-1]


class QueueList:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def front(self):
        return self.items[0]

    def back(self):
        return self.items[-1]

    def is_empty(self):
        return not len(self.items)

    def __str__(self):
        return str(self.items)

    @staticmethod
    def challenge():
        myq = QueueList()
        myq.enqueue(5)
        myq.enqueue(4)
        myq.enqueue(2)
        myq.enqueue(3)
        print(myq)
        print(myq.dequeue())
        print(myq)


class QueueLinkedList:
    pass


class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return self.items


if __name__ == "__main__":
    # Stack.challenge()
    QueueList.challenge()
