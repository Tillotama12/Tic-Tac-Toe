#membership operator
#in and not in

list1=[1,3,5,7,9,11]

print(5 in list1)
print(5 not in list1)
print(6 in list1)
print(6 not in list1)

if True:
    print("Hello")

print("Enter the value:")
x=int(input())

if (x in list1):
    print("found")
else:
    print("not found")

students={1:"ram",2:"raj",3:"rahul",4:"shaym"}

#using dictionary
print(4 in students)
print("ram" in students)

message="Hello Edubridgers"
print("Hello" in message)
print("hello" in message)
print("Edubridge" in message)
print(" " in message)

