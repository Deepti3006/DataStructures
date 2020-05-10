class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self,data):
        if data <self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def findtheNumber(self,findNumber):
        if findNumber < self.data :
            if self.left is None:
                return str(findNumber) + "not Found"
            return self.left.findtheNumber(findNumber)
        elif findNumber >self.data:
            if self.right is None:
                return str(findNumber) + "Not Found"
            return self.right.findtheNumber(findNumber)
        else:
            print(str(self.data)+ "is found")

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()
root = Node(20)
root.insert(10)
root.insert(30)
root.PrintTree()
root.findtheNumber(10)
root.findtheNumber(40)