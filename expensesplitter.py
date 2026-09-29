def calculate():
    while True:
        bill=input("Total Bill: ")
        tip=input("Tip Percentage: ")
        if bill.isdigit() and tip.isdigit():
            bill=int(bill)
            tip=int(tip)
            break
        else:
            print("Invalid Typing")
    total_bill=bill+(bill*(tip/100))
    return total_bill


def final_cal(people,each_payout):
    result={}
    for i in range(people):
        person=input("Person: ")
        paid=float(input(f"{person} paid: "))
        final=each_payout-paid
        result[person]=final
    for person in result:
        if result[person]>0:
            print(f"{person} owes {result[person]:.2f}")
        elif result[person] < 0:
            print(f"{person} should receive {-result[person]:.2f}")
        else:
            print(f"{person} has paid exactly their share")



def main():
    people=int(input("How many people: "))
    total_bill=calculate()
    each_payout=total_bill/people
    print(f"Everyone should pay: {each_payout:.2f}")
    final_cal(people,each_payout)


main()