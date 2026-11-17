'''
2. Multi Stage Prime Lock System


A smart locker opens only if final derived number is prime.


Write a program to:


- Find sum of digits

- Find product of digits

- Find difference between product and sum

- Count digits in difference

- Add digit count to difference

- Check whether final result is Prime or Not
'''
n=int(input("Number = "))
sum=0
pro=1
count=0
while n>0:
	r=n%10
	sum=sum+r
	pro=pro*r
	n=n//10
diff=pro-sum
x=diff
print("Sum of Digit = ",sum)
print("Product Of Digit = ",pro)
print("Difference = ",diff)
while diff>0:
	diff=diff//10
	count=count+1
print("Count digit in Difference = ",count)
add=count+x
print(add)
i=2
count=0
while add>i:
	if add%i==0:
		count=count+1
		break
	i=i+1
if count==0:
	print("Print Number")
else:
	print("Not Prime Number")
		 