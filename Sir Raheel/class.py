class person: # Parent Class
    def __init__(self, name , age , gender , income):
        self.name = name
        self.age = age
        self.gender = gender
        self.income = income
    def PersonInfo(self):
        print('Name :- {}'.format(self.name))
        print('Age :- {}'.format(self.age))
        print('Gender :- {}'.format(self.gender))
        print('income :- {}'.format(self.income))



class student(person): # Child Class
    def __init__(self,name,age,gender,income,studentid,fees):
        person.__init__(self,name,age,gender,income)
        self.studentid = studentid
        self.fees = fees

    def StudentInfo(self):
        print('Student ID :- {}'.format(self.studentid))
        print('Fees :- {}'.format(self.fees))


stud1 = student('Asif' , 24 , 'Male' , 100 , 123 , 1200)
print('Student Details')
print('---------------')
stud1.PersonInfo() # PersonInfo() method presnt in Parent Class will be access
stud1.StudentInfo()
print()