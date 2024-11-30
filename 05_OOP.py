'''
def checkStudentSuccess(name,score):
    if score>=90:
        print("{} has excellent level".format(name))
    elif 75<=score<90:
        print("{} has good level".format(name))
    elif 60<=score<75:
        print("{} has average level".format(name))
    else:
        print("{} has poor level".format(name))


def checkPupilSuccess(name,score):
    if score>=10:
        print("{} has excellent level".format(name))
    elif 7<=score<10:
        print("{} has good level".format(name))
    elif 4<=score<7:
        print("{} has average level".format(name))
    else:
        print("{} has poor level".format(name))

checkStudentSuccess("Jane",78)
checkPupilSuccess("Bob",6)

userLogs=['Admin123','superUSER','GOODstudent']

userBYears=[2000, 2010, 2005]

def listMaker1(myList):
    result=[]
    for item in myList:
        result.append(item.lower())
    return result


def listMaker2(myList):
    result=[]
    for item in myList:
        result.append(2024-item)
    return result

newList1=listMaker1(userLogs)
newList2=listMaker2(userBYears)
print(newList1)
print(newList2)

newList1=listMaker1(userBYears)
newList2=listMaker2(userLogs)
print(newList1)
print(newList2)
'''
'''
#int a = 10;
#int b;
a = 10#4b --- int
print(a)
# b#?????????
# print(b)
b= 10
print(b)

class Student:
    #attrubute
    spec="Computer science"
    def __init__(self,name,age):
        #properties
        self.name = name
        self.age = age

    def showInfo(self):
        return f"Student {self.name} is {self.age} years old."
    
    def showMsg(self,msgText):
        return f'Student {self.name} says {msgText}'

student1 = Student("Bob",20)#default constructor
student2 = Student("Jane",15)#default constructor
print(student1.name)
print(student1.age)

print(student2.name)
print(student2.age)
print(student1.showInfo())
print(student2.showInfo())
print(student1.showMsg("Hello"))
print(student2.showMsg("Hi"))
#public private protected
'''
import random
# class Person:
#     def __init__(self,firstname,lastname,age):
#         #public properties
#         self.firstname = firstname
#         self.lastname= lastname
#         self.age=age

#         #private
#         #__privateProp
#         #__privateMethod()
#         self.__personId = random.randint(1,100)
#     #private method
#     def __getId(self):
#         return f"{self.__personId}"
#     #public methods
#     def getInfo(self):
#         return f"{self.__getId()}. Person first name - {self.firstname};last name - {self.lastname};age - {self.age}."
    
#     def getHi(self, msgText):
#         personalInfo = self.getInfo()
#         return f"{personalInfo}\n{msgText}! I am {self.firstname}."


# person = Person("Joe","Black",44)
# print(person.getInfo())
# person.age = 35
# print(person.getInfo())
# #print(person.__personId)
# person.__personId = 100
# print(person.__personId)
# #person.__getId()
# print(person.getHi("How are you?"))

class Person:
    def __init__(self,firstname,lastname,age):
        #public properties
        self.firstname = firstname
        self.lastname= lastname
        #protected
        self._age=age
        #private properties
        self.__personId = random.randint(1,100)
    def __getId(self):
         return f"{self.__personId}"
    
    #protected methods
    def _getFullName(self):
        return f"Person full name:{self.firstname}{self.lastname}"
    
    def getInfo(self):
        return f"{self.__personId} Person first name - {self.firstname};last name - {self.lastname};age - {self._age}."
    
    def getHi(self, msgText):
        personalInfo = self.getInfo()
        return f"{personalInfo}\n{msgText}! I am {self.firstname}."
    
    #static methods
    @staticmethod
    def sayGreetings():
        print("Nice to meet you!")

    #class methods
    @classmethod
    def setDefaultHobby(cls):
        cls.hobby="Drawing"
    
person1 = Person("Joe","Black",25)
person2 = Person("Kate","Smith",18)

Person.setDefaultHobby()
print(person1.hobby)
person1.sayGreetings()
print(person1.getHi("Hello"))
print(person2.getHi("Hi"))


class Student(Person) :
    spec = "Computer Science"

    def __init__(self, firstname, lastname, age, averageMark):
        super().__init__(firstname, lastname, age)#Person(firstname, lastname, age)
        self.averageMark = averageMark

    #averageMark
    def isSuccessful(self):
        return True if self.averageMark>= 75 else False
    
    def getInfo(self):
        return super().getInfo()+ f'\nSpec : {self.spec}. Average mark : {self.averageMark}'


student1 = Student("Kolya","Muxaluk",14,85)
#print(student1.getHi("Hello. I am Mukola"))
print(student1.getInfo())
print(f"Is {student1.firstname} success student? {student1.isSuccessful()}")

# class Employee(Person):
#     def __init__(self, firstname, lastname, age, position, salary,experiance):
#         super().__init__(firstname, lastname, age)
#         self.position = position
#         self.salary = salary
#         self.exp = experiance

#     def getInfo(self):
#         return super().getInfo()+f"\n{self.position} {self.salary} {self.exp}"
    
#     def getSickLeavePerc(self):
#         if self.exp>5:
#             return 1
#         elif 3<self.exp<=5:
#             return 0.75
#         else:
#             return 0.5
        
# employee1 = Employee("Olga","Ivanchuk",26,"C# developer",2500,2)

# print(employee1.getInfo())
# print(employee1.getHi("Hello"))

class Employee(Person):
    def __init__(self, firstname, lastName, age, salary):
            super().__init__(firstname, lastName, age)
            self.salary = salary
    def isRetiree(self):
        print(self.getInfo())
        if self._age>60:
            print(f"{self.firstname} is retiree")
        else:
            print(f"{self.firstname} is not retiree")

    def showEmployeeID(self):
        print(self.__personId)

    def changeAge(self, newAge):
        self._age=newAge

employee1=Employee("Joe","Black",65, 3000)
employee1.isRetiree()
#employee1.showEmployeeID()

employee1.changeAge(35)
employee1.isRetiree()

print(employee1._getFullName())
