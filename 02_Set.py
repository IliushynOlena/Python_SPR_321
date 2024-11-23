
#A = {a,b,c.....z}
#S1 = {Bob, Kate, Jon}

#set - unique
'''
a = 10
str = 'hello'
str = 'gggg'
flag = True
arr= [1,2,3,65,5]

mySet1 = {15,2,3,4,5,15,2,3,4,5}
mySet2 = {'Joe','Kate','Bob','Kate','Bob'}
mySet3 = {23,'Bob',False,(45.2, 12)}
mySet4 = set((10,40,12,30))
print("my Set 1 - set of number : ", mySet1)
print("my Set 2 - set ofn strings : ", mySet2)
print("my Set 3 - set of mixed elements : ", mySet3)
print("my Set 4 : ", mySet4)
allUsers = ['Joe','Kate','Bob','Kate','Bob']
uniqueUserName = set(allUsers)
print(allUsers)
print(uniqueUserName)

# passwordsSet = {'111',['222','333']}#error
# print(passwordsSet)
myEmptySet = set()
print(type(myEmptySet))

mySetA = {1,2,3}
mySetB = {3,2,1}

print(mySetA == mySetB)
print(mySetA)
print(mySetB)
usersName = {'Joe','Kate','Bob','Kate','Bob'}
#foreach
for name in usersName :
    print(name)

name = input("Enter your name: ")
if name in usersName:
    print("Welcome",name)

for(int = 0; i < usersName.Lenght; i ++)
{
    usersName[i] ="kdksdhsd";//set
    print( usersName[i] );//get
}



word = input("Enter your word: ")
for letter in word:
    print(letter)

for letter in set(word):
    print(letter)

'''
mySet =  {1,2,3}
print(mySet)

mySet.add(4)
print(mySet)

mySet.update([3,4,5])
print(mySet)

mySet.update([5,6,7],{8,9})
print(mySet)

mySet.discard(4)
print(mySet)

mySet.discard(10)
print(mySet)

mySet.remove(1)
print(mySet)

# mySet.remove(10)
# print(mySet)
mySet.clear()
print(mySet)
# & , intersection()
# |, uniou()
# -, difference()

usersName1 = {'Hanna','Kate','Bob',}
usersName2 = {'Joe','Kate','Jack','Jane','Bob'}

print("Student group 1: " , usersName1)
print("Student group 2: " , usersName2)

print(usersName1&usersName2)
print(usersName1.intersection(usersName2))

print(usersName1|usersName2)
print(usersName1.union(usersName2))

print(usersName1-usersName2)
print(usersName1.difference(usersName2))

print(usersName2-usersName1)
print(usersName2.difference(usersName1))


studSet={'Bob','Joe','Jane','Kate','Jack'}
print(f"We have {len(studSet)} students in our group.")
print("Min score is", min(studSet))
print("Max score is", max(studSet))

for ind,item in enumerate(studSet):
    print(ind,item)

scores={1,2,3,4,5,6,7,8,9,10,11,12}
#scores[0] = 100#error
print("Min score is", min(scores))
print("Max score is", max(scores))
print("Sum of scores:", sum(scores))

