import math
class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self,data):
        arr = []

        if data < self.data:
            if self.left is None:
                self.left = Node(data)
                return arr.append(self.left)
            else:
                self.left.insert(data)
                return arr.append(self.left)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
                return arr.append(self.right)
            else:
                self.right.insert(data)
                return arr.append(self.right)
        else:

            return arr.append(self.data)
        return arr








    def findElemInLinear(self,elem):
        if elem < self.data:
            if self.left is None:
                return str(elem) +"not found"
            return self.left.findElemInLinear(elem)
        elif elem >self.data:
            if self.right is None:
                return print(str(elem) + "not found")
            return self.right.findElemInLinear(elem)
        else:
            return print("Value found "+ str(elem))

    def size(self):
        total = 1  # any instantiated object has a size of at least 1.
        if self.left is not None:  # feel free to add additional validity checks, i.e. instanceof(Tree...)
            total += self.left.size()
        if self.right is not None:
            total += self.right.size()
        #print(total)
        return total

    def printTree(self):
        if self.left:
            self.left.printTree(),
        print(self.data)
        if self.right:
            self.right.printTree()


#Doing it liner wayy
def findEleminGivenArray(a,l,r,x):

        while l <= r:
            mid = l+(r-1) // 2
            print(mid)
            if a[mid] == x:
                return mid
            elif a[mid] < x:
                l = mid + 1
            else:
                r =mid -1
        return -1
#Doing binary serach in recusion

def findelementBinarySearchRecurion(arr,l,r,x):

    if r >= l:
        mid = l+(r-1)//2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return findelementBinarySearchRecurion(arr,l,mid-1,x)
        else:
            return findelementBinarySearchRecurion(arr,mid+1,r,x)
    else:
        return -1





n = Node(40)
n.insert(30)

n.insert(50)
n.printTree()
n.findElemInLinear(40)
n.findElemInLinear(30)
n.findElemInLinear(80)
total = n.size()
print(total)
arr = [1,2,3,6,7,8]
l = 0
r = len(arr) -1
x=8
result = findEleminGivenArray(arr, l, r, x)
if result != -1:
    print("Number found % d" % result + str(arr[result]))
else:
    print("Number is not found")
result = findelementBinarySearchRecurion(arr, l, r, x)
if result != -1:
    print("Number found % d" % result + str(arr[result]))
else:
    print("Number is not found")
