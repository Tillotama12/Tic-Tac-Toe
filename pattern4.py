rows=int(input("rows:"))

for i in range(rows+1):
    for j in range(i):
        print(i,end=" ")
    print()


rows=int(input("rows:"))

for i in range(rows+1):
    for j in range(i,i+1):
        print(j,end=" ")
    print()