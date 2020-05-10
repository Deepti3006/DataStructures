class interviewProgramme:

    def __init__(self, wordtotest):
        print("Nothing:")
        self.wordtotest = wordtotest

    def isPallindrome(self):

        revwordtotest = self.wordtotest[::-1]
        print(revwordtotest)
        if self.wordtotest == revwordtotest:
            print("I am a pallindrome")
        else:
            print("I am not pallindrome")

    def countUpper(self):
         count =0
         for i in range(len(self.wordtotest)):
             print(self.wordtotest[i])
             capitalTest = self.wordtotest[i]
             if capitalTest.isupper():
                 count =count +1
                 print("I am capital " + capitalTest)
                 print("count is" + str(count))
             print ("count is " + str(count) + "and the word is " + capitalTest)



inp = interviewProgramme("I am testing you")
inp.isPallindrome()
inp.countUpper()


