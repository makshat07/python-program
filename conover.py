class student:
    def __init__(self,a=11,b="akshat"):
        self.rollno=a
        self.name=b
    def printvalues(self):
        print("rollno=",self.rollno)
        print("name",self.name)
    
s1=student()
s1.printvalues()
s1=student(7,"anish")
s1.printvalues()
        
        
