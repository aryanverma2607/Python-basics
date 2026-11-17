'''3. E-Commerce Offer Engine
   An online store provides multiple offers independently:

* If cart value ≥ 500 → Free delivery
* If cart value ≥ 1000 → 10% discount coupon
'''
cart_value=float(input("Enter Cart Value:"))
if cart_value>=500:
	print("Free delivery")
	if cart_value>=1000:
		print("10% Discount Coupon")
else:
	print("No Offer Available")