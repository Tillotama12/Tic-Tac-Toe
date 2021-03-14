rows=int(input("Enter the number of rows: "))
n=(2*rows)-2

for i in range(0,rows):
    for j in range(0,n):
        print(end=" ")
    n=n-1

    for j in range(0,i+1):
        print("*",end=' ')

    print()

hw-reverse equilateral traingle
