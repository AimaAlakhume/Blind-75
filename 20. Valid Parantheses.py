class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def pop(self):
        self.items.pop()

    def push(self, value):
        self.items.append(value)

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]

    def size(self):
        return len(self.items)

class Solution:
    def isValid(self, s: str) -> bool:
        storeStack = Stack()
        balanced = True
        ind = 0
        while ind < len(s) and balanced:
            symbol = s[ind]
            if symbol in '[({':
                storeStack.push(symbol)
            else:
                recent = storeStack.peek()
                if (recent == '(' and symbol == ')') or (recent == '[' and symbol == ']') or (recent == '{' and symbol == '}'):
                    storeStack.pop()
                else:
                    balanced = False
            ind += 1
        if storeStack.isEmpty() and balanced:
            return True
        return False
