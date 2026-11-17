print("Mobile EMI Calculator")
Mobile_price=int(input("Mobile price="))
Down_payment=int(input("Down payment="))
interest_rate=int(input("Enter interest rate="))
months=int(input("Enter months="))
remaining_amount=Mobile_price - Down_payment
interest=((remaining_amount*interest_rate*(months/12))/100)
total=interest+remaining_amount
print("Remaining Amount={}".format(remaining_amount))
print("Total with Interest={}".format(total))
print("Monthly EMI=",total/months)


