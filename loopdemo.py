#infinite loop
#while True:
  #  print("hello")


#finite while loop

#initialization
# count=0
#
# while count<5:
#     print("count is",count)
#     count+=1
#
# print("exit the loop")

#for loop

# name="school of coding"
# for letter in name:
#     print(letter)

batches=[5016,5020,5021]

for batch in batches:
    print("batch code is",batch)

for batch in batches:
    if batch==5021:
        print("batch code found")
        break;
    else:
        print("batch code is",batch)