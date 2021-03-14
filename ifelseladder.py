# #if elif
# print("enter the num")
# num=int(input())
#
# if num==5016:
#     print("Thane soc")
# elif num==5020:
#     print("pune soc")
# elif num==5021:
#     print("chennai soc")
# else:
#     print("Edubridge emp/guest")

#nested if

# print("validating age..pls anter age")
# age=int(input())
#
# if(age>=18):
#     print("major")
# else:
#     print("minor")

print("validating age..pls anter age")
age=int(input())

nationality="indian"

if(age>=18):
    if(nationality=="indian"):
        print("valid voter.")
    else:
        print("not valid for vote")
else:
    print("minor")

