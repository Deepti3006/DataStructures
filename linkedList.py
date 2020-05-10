class Node:
    def __init__(self,dataval):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval =None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    def AtBegining(self, newdata):
        NewNode = Node(newdata)
        # Update the new nodes next val to existing node
        NewNode.nextval = self.headval
        self.headval = NewNode

    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        # Update the new nodes next val to existing node
        laste = self.headval
        while (laste.nextval):
            laste = laste.nextval
        laste.nextval = NewNode

    def Inbetween(self, middle_node, newdata):

        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode


list1 = SLinkedList()
list1.headval = Node(30)
e2 = Node(40)
e3 = Node(50)
list1.headval.nextval = e2
e2.nextval = e3
list1.AtBegining(10)
list1.AtEnd(100)
list1.Inbetween(e3,60)
list1.listprint()



