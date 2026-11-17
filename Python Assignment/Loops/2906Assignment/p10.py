'''
10.Zero Count Prime Scanner
A banking system checks account numbers.
Write a program to:
- Count zero digits
- Find sum of digits
- Add zero count and sum
- Multiply by smallest digit
- Check whether final result is Prime or Not

Input:
908406

Output:
Zero Count = 2
Sum = 27
Smallest Digit = 0
Final Result = 0
Not Prime
'''
n=input("Enter number = ")
l=len(n)
m=int(n)
sum=0
count=0
smallest=9
for i in n:
	if i=="0":
		count=count+1
print("Zero Count = ",count)
while m>0:
	r=m%10
	sum=sum+r
	if smallest>r:
		smallest=r
	m=m//10
print(f"Sum = {sum}")
print("Smallest Digit= {}".format(smallest))
new=sum*smallest
print("Final Result = ",new)
i=2
while i<=new:
	if new%i==0:
		count=count+1
	i=i+1
if count==0:
	print("Prime Number")
else:
	print("Not Prime Number")