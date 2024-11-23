#Dictionary

#['Joe', 'Smith', 25, 'admin25', '10.01.2022']

# D = {
#     <key1>: <value1>,
#     <key>2: <value2>,
#     .
#     .
#     .
#     <keyM>: <valueM>
# }

myDict1= {
    'key1': 1, 
    'key2': 20.5, 
    'key3': True
    }
myDict2= {
    1: 'student',
    2: 'admin'
}
print(myDict1) #{'key1': 1, 'key2': 20.5, 'key3': True}
print(myDict2) #{1: 'student', 2: 'admin'}

bookDict = {
'author':'Eric Matthes',
'title':'Python Crash Course',
'price':14.43,
'reading age':'12 years and up',
'language':'English'
}

print(bookDict.get('author'))
print(bookDict.get('title'))
print(bookDict.get('price'))
print(bookDict.get('pages'))
print(bookDict['author'])
print(bookDict['title'])
print(bookDict['price'])
#print(bookDict['pages'])
'''
infoType = input("What info do you want to know aboutthe book?")
if infoType in bookDict:
    print(bookDict[infoType])
else:
    print("Sorry!")


for dictKey, dicVal in bookDict.items():
    print(F"{dictKey}:{dicVal}")

bookDict['pagesN']= 350

for dictKey, dicVal in bookDict.items():
    print(F"{dictKey}:{dicVal}")

newInfo=input("What info about the book do you want to add?")
if newInfo!="": 
    newInfoValue=input(f"Input value for the key'{newInfo}':")
    if newInfoValue!="":
        bookDict[newInfo]=newInfoValue
    else:
        print("No value for the key '{}':".format(newInfo))
else:
    print("No key!")
bookDict[newInfo] = "Kyiv"
for dictKey, dicVal in bookDict.items():
    print(F"{dictKey}:{dicVal}")
'''
'''
print(len(bookDict))
print(bookDict)
myDict3 = dict([("a", 111), ("b", 222)])
print(myDict3)

myDict4 = dict([["a", 111], ["b", 222]])
print(myDict3)

myDict5 = dict(['qw', 'er', 'ty'])
print(myDict5) #{'q': 'w', 'e': 'r', 't': 'y'}

keyList=['a','b']
valueList=[111,222]
myDict6=dict(zip(keyList,valueList))
print(myDict6) #{'a': 111, 'b': 222}

myDict7=dict(firstName='Joe', lastName='Smith')
print(myDict7) #{'firstName': 'Joe', 'lastName': 'Smith'}

myEmptyDict1={}
print(myEmptyDict1) #{}
myEmptyDict2=dict()
print(myEmptyDict2) #{}
'''