class Student:
    course = "13COM"
    def __init__(self,name,test1=0,test2=0):
        self.name = name
        self.test1 = test1
        self.test2 = test2
    def compute_average(self):
        return ((self.test1 + self.test2)/2)
    def print_data(self):
        print("The grade for %s in %s is %4.1f % \")
        (self.name,self.course,self.compute_average())


David = Student("David",90,100)
Bob = Student("Bob",60,80)
David.print_data()
Bob.print_data()