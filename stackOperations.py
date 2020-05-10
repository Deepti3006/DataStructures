class Stack:

    def __init__(self):
        self.stack = []

    def add(self,dataval):

        if dataval not in self.stack:
            self.stack.append(dataval)
        print(str(print(self.stack)))

    def remove(self):
        self.stack.pop()

S = Stack()

print(S.add(20))
S.add(30)
S.add(50)
S.add(60)
S.remove()
print(S.remove())