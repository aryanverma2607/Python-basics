print("Restaurant Bill Split")
amount=int(input("Enter Total Bill="))
friends=int(input("Enter number of friends="))
gst=amount*0.05
scharge=amount*0.1
total=amount+gst+scharge
eachpay=total/friends
print(f"Final Bill={total}")
print("Each Person Pays={}".format(eachpay))
print("---------------------------------------")