class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                self.left = Node(data)
            elif data > self.data:
                self.right = Node(data)
        else:
            self.data = data

    def findval(self, valtofind):
            if valtofind < self.data:
                if self.left is None:
                    return str(valtofind) + "not found"
                return self.left.findval(valtofind)
            elif valtofind > self.data:
                if self.right is None:
                    return str(valtofind)+"not found"
                return self.right.findval(valtofind)
            else:
                print(str(self.data) + "is found")


    def printTree(self):
        if self.left:
            self.left.printTree(),
        print(self.data)
        if self.right:
            self.right.printTree()

root = Node(10)

root.insert(8)
root.insert(30)
print(root.findval(8))
print(root.findval(40))

root.printTree()