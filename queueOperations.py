class queue:

    def __init__(self):
        self.queue = []

    def add(self, dataval):

        if dataval not in self.queue:
            self.queue.insert(0,dataval)
        print(str(print(self.queue)))
    def remove(self):
            self.queue.pop()

q =queue()
q.add(20)
q.add(30)
print(q.remove())