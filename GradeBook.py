class Gradebook():
    def __init__(self,gradebook = [{"Name": "Jarred", "Grade": "A"}, {"Name": "Harred", "Grade": "C"}]):
        self.gradebook = gradebook

    def addGrades(self, name, grade):
        self.gradebook.append({"Name" : name, "Grade": grade})

    def checkGrades(self):
        for x in range(len(self.gradebook)):
             print (self.gradebook[x])

gradebook1 = Gradebook()
#gradebook1.addGrades(input("What is their name?"), input("What is their grade?"))

gradebook1.checkGrades()
