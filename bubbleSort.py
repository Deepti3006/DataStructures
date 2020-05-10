class bubbleSort():
    # In this sorting adjecent elements are compared an
    # then sorting is done.-->
    def sortbubble(self):
        sum = int(input(("Please enter total number of elements")))
        a =[]
        for i in range(sum):
            element = int(input("please enter the value of element"))
            a.append(element)
        # Bubble sort
        print(a)
        for i in range(len(a)):
            for y in range(len(a)-1):
                if a[y] > a[y+1]:
                    a[y], a[y+1] = a[y+1], a[y]

        print("Array after sort:" + str(a))

bb =bubbleSort()
bb.sortbubble()
