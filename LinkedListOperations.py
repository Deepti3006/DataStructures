class Node():

    def __init__(self,dataval):
        self.dataval = dataval
        self.nextval = None

class SLinkedList():

    def __init__(self):
        self.headval=None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    def size_of_list(self):
        current = self.headval
        count=0
        while current:
            count = count+1
            current= current.nextval
        return count

    def insertinBeginning(self,newval):

        NewNode = Node(newval)
        NewNode.nextval = self.headval
        self.headval = NewNode

    def insertatEnd(self,endval):
        endnode = Node(endval)
        last = self.headval
        while last.nextval:
            last = last.nextval
        last.nextval = endnode

    def insertatMiddle(self,middleNode,newNode):
        NewNode = Node(newNode)
        NewNode.nextval = middleNode.nextval
        middleNode.nextval = NewNode



list1 = SLinkedList()
list1.headval = Node(30)
e2=Node(40)
e3=Node(50)
list1.headval.nextval = e2
e2.nextval = e3
list1.listprint()
count=list1.size_of_list()
#temp = list1.headval
#list1.headval = e3
#e3=temp

#print(list1.headval.dataval)
#print(e2.dataval)
#print(e3.dataval)

list1.insertinBeginning(10)
list1.insertatEnd(60)
list1.insertatMiddle(e3,25)
list1.listprint()




