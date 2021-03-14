try:
    print("outer try block")
    print("second line")
    print("i am jumping directly to the outer except block")
    print("third line")
    #print(10/0)
    try:
        print("fifth line")
        print("sixth line")
        print(10/0)
        print("seventh line")

    except:
        pass
       # print("please enter valid denominator")
    print("welcome")
except:
    print("please enter a proper denominator")

finally:
    print("clean up code")