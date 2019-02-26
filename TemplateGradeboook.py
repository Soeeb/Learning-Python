#Sample Output
#Given name John, Family name Martins
#Standard: 91906, result E
#Standard: 91903, result E
#Standard: 91905, result E

class Result:
    #When a student sits a standard, they get get a result
    def __init__(self, standard, grade):
        self.standard = standard
        self.grade = grade

    def point_value(self, grade, credits):
        if grade == "E":
            return credits*4
        elif grade == "M":
            return credits*3
        elif grade =="A":
            return credits*2
        elif grade =="NA":
            return credits*1

    def display(self):
        print("Standard: %s, result %s" % (self.standard.standard_number, self.grade))

class Standard:
    def __init__(self, title, standard_number, version, credit_value):
        self.title = title
        self.standard_number = standard_number
        self.version  = version
        self.credit = credit_value
#NZQA standards

class Student():
    results = [ ]

    #Individual student, incorporating their NZQA results
    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name

    def display(self):
        print ("Given name %s, Family name %s" % (self.given_name, self.family_name))
        for result in self.results:
            result.display()
    #Also calculate their total Grade point score and display it

#create arrays we could append test data
students = [ ]
standards = [ ]

#append test data to student
students.append(Student("John", "Martins"))
#append test data to standards
standards.append(Standard("Programming", 91906, 6, 1))
#append data to results, note how indexing 
students[0].results.append(Result(standards[0], "E"))
# display data
for student in students:
    student.display()
