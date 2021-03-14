#atm

atm_pin="4567"
pin_count=0
pin_limit=3
pin=""
out_of_guess=False
total_amount=6000

print("welcome to canara bank")
while pin!=atm_pin and not(out_of_guess):
    if pin_count<pin_limit:
        pin=int(input("enter your pin"))
        pin_count+=1
        if pin==atm_pin:
            withdraw=int(input("Enter the amount:"))
            if withdraw<total_amount:
                balance=total_amount-withdraw
                print("availble balance is",balance)
            else:
                print("not sufficient amount")
        else:
            out_of_guess=True
if out_of_guess:
    print("your card is blocked")
    print("thank you for using atm")