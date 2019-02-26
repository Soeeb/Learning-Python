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

    def point_value(self):
        credit = self.standard.credit_value
        if self.grade == "E":
            return credit*4
        elif self.grade == "M":
            return credit*3
        elif self.grade =="A":
            return credit*2
        elif self.grade =="N":
            return credit*1

    def display(self):
        print("Standard: %s, result %s" % (self.standard.standard_number, self.grade))

class Standard:
    def __init__(self, title, standard_number, credit_value, version):
        self.title = title
        self.standard_number = standard_number
        self.version  = version
        self.credit_value = credit_value
#NZQA standards

class Student():

    #Individual student, incorporating their NZQA results
    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.results = []

    def display(self):
        print ("Given name %s, Family name %s" % (self.given_name, self.family_name))
        for result in self.results:
            result.display()
    #Also calculate their total Grade point score and display it
    def rank_score_calc(self):
        rank_score = 0
        for result in self.results:
            rank_score += result.point_value()
        return rank_score
#create arrays we could append test data
students = [ ]
standards = [ ]

#append test data to student
students.append(Student("John", "Martins"))
#append test data to standards
standards.append(Standard("Programming", 91906, 6, 1))
#append data to results, note how indexing 
students[0].results.append(Result(standards[0], "E"))
#Test data
students.append(Student("Philip", "Lin"))
students.append(Student("Michael", "Brown"))

standards.append(Standard("Programming", 91906, 6, 1 ))
standards.append(Standard("Database", 91902, 4, 1))
standards.append(Standard("Website", 91903, 4, 1))
standards.append(Standard("Networking", 91905, 4, 1))

students[1].results.append(Result(standards[0], "E"))
students[1].results.append(Result(standards[2], "E"))
students[1].results.append(Result(standards[3], "E"))
students[2].results.append(Result(standards[3], "A"))
students[2].results.append(Result(standards[1], "N"))

# display data
for student in students:
    student.display()

print(students[1].rank_score_calc())
#print(Result.point_value(students[0].results, students[0].results.standard.credit_value))
