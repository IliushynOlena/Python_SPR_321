
# a = 10
# print(f'a = {a}')
# a = "Hello"
# print(f'a = {a}')

#b = input('Enter number b : ')#intput -> str
# b = int(input('Enter number b : ')) 

# print(f"Summa = {a+b}")

# def printHello():
#     print("Hello world")

# printHello()

# def HelloUser(name):
#     print(f"Hello, {name}")


# HelloUser("Olena")
# HelloUser("Dima")

# def HelloAdmin(name = "admin"):
#     print(f"Hello, {name}")

# HelloAdmin('Yura')
# HelloAdmin()
'''
num1 = 1
print(f'{num1} is of type {type(num1)}')

num2 = 3.36
print(f'{num2} is of type {type(num2)}')

num3 = 2 + 4j
print(f'{num3} is of type {type(num3)}')

num4 = 'Python'
print(f'{num4} is of type {type(num4)}')

#list
languages = ['Docker','Java','Python', 45, 3.36, True]
print(languages[0])
print(languages[1])
print(languages[2])
print(languages[3])
print(languages[4])
print(languages[5])

#tuple (conrtege)
product = ("Sony","Playstation",599.99)
print(product)
print(product[0])
print(product[1])
print(product[2])

#set (mnozunu)
student_id = {112,114,116,118,115}
print(student_id)
#print(student_id[0])- error

#dic 
capital_city = {
    "Ukraine":"Kyiv",
    "Spain":"Madrid",
    "Japan":"Tokio"
    }
print(capital_city)
print(capital_city["Ukraine"])
#print(capital_city["Kyiv"]) error

###### Tuple #####
userTypes = ["admin","student","teacher"]
print(userTypes)

userTypes[0] = 'user'
print(userTypes)

myEmptyTyple1 = ()
myEmptyTyple2 = tuple()

print(myEmptyTyple1)
print(type(myEmptyTyple1))

print(myEmptyTyple2)
print(type(myEmptyTyple2))

myTuple1 = ('element1',12,36.5,False)
myTuple2 = ('item1',)
userTypes = 'admin','student','teacher'
userName ='Jane',
print(f'{myTuple1} . type : {type(myTuple1)}')
print(f'{myTuple2} . type : {type(myTuple2)}')
print(f'{userTypes} . type : {type(userTypes)}')
print(f'{userName} . type : {type(userName)}')

nameTypes = tuple(("Alex","Helen"))
print(f'{nameTypes} . type : {type(nameTypes)}')

userTypes = 'admin','student','teacher'
print(f'1 user : {userTypes[0]}')
print(f'2 user : {userTypes[1]}')
print(f'1 user : {userTypes[-1]}')
print(f'2 user : {userTypes[-2]}')
print(f'Len : {len(userTypes)}')
print(f'Last element : {userTypes[len(userTypes)-1]}')
#range - diapazon
print(f'1th two user : {userTypes[0:2]}')
print(f'1th two user : {userTypes[:2]}')
print(f'1th two user : {userTypes[:]}')
print(f'1th two user : {userTypes[1:3]}')

#userTypes[0] = "user" - erroe
print(userTypes)
del userTypes
#print(userTypes)

userTypes = 'admin','student','teacher','moderator'
user1, user2, user3, user4 = userTypes
print(user1)
print(user2)
print(user3)
print(user4)


userTypes = 'admin','student','teacher','moderator'
user1, *users = userTypes
print(user1)
print(users)


userTypes = 'admin','student','teacher','moderator'
user1, *users, lastuser = userTypes
print(user1)
print(users)
print(lastuser)
#foreach
for user in userTypes:
    print(user, end=" ")
print()

#for
for i in range(len(userTypes)):
    print(userTypes[i])


userTypes1 = 'admin','student','teacher','moderator'
userTypes2 = ('user1','user2')
allUsers = userTypes1 + userTypes2
for user in allUsers:
    print(user)
print("------------------------------------------------------")
for user in allUsers*2:
    print(user)
print(userTypes1.count('admin'))
print(userTypes1.index('admin'))

if 'student' in userTypes1:
    print("student is correct login")
    '''
def askPersonalInfo():
    while True:
        firstName=input("Input your first name:")
        lastName=input("Input your last name:")
        yearBirth=input("Input your year of birth:")
        gender=input("Input your gender (M,F):")
        if firstName=="" or lastName=="" or yearBirth=="" or gender=="" or gender not in ('F','M'):
            print("Wrong data!")
        else:
            return firstName, lastName, yearBirth,gender

#personalInfo=askPersonalInfo()
#print(personalInfo)

def askAdditionalInfo(queryStr):
    infoInd=1
    infoList=[]
    while True:
        infoName=input("Name of the {} #{}:".format(queryStr,infoInd))
        if infoName=="":
            print("No info. Input stopped.")
            break
        else:
            infoList.append(infoName)
            infoInd+=1
    if len(infoList)>0:
        if queryStr=='hobby':
            print("You have {} hobbies.".format(infoInd-1))
        elif queryStr=='programming languages':
            print("You know {} programming languages.".format(infoInd-1))
    else:
        print("You have no info at all")
    return infoList
userInfo=[]
userInfo.append(askPersonalInfo())
userInfo.append(askAdditionalInfo('hobby'))
userInfo.append(askAdditionalInfo('programming languages'))
print(userInfo)

