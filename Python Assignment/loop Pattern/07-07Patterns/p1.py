#1.****
'''n=int(input("Enter number = "))
for i in range(n+1):
	print("*",end="")

2.
*
*
*
*
*
n=int(input("Enter number = "))
for i in range(n+1):
	print("*")

#3.
*
 *
  *
   *
    *

n=int(input("Enter number = "))
for i in range(n):
	for j in range(n):
		if j!=i:
			print(" ",end="")
		else:
			print("*")
	print()

4.
******
******
******
******
******

n=int(input("Enter number = "))
for i in range(n):
	for j in range(n):
		print("*",end="")
	print()

5.
12345
12345
12345
12345
12345

n=int(input("Enter number = "))
for i in range(n):
	for j in range(1,n+1):
		print(j,end="")
	print()

#6.
11111
22222
33333
44444
55555

n=int(input("Enter number = "))
for i in range(1,n+1):
	for j in range(1,n+1):
		print(i,end=" ")
	print()

7.
1
00
111
0000
11111
n=int(input("Enter number = "))
i=1
while i<=n:
	j=1
	while j<=i:
		if i%2==0:
			print("0",end=" ")
		else:
			print("1",end=" ")
		j=j+1
	print()
	i=i+1
8.
*
**
***
****
*****
n=int(input("Enter number = "))
i=1
while i<=n:
	j=1
	while j<=i:
		print("*",end="")
		j=j+1
	print()
	i=i+1

9.
1
12
123
1234
12345
n=int(input("Enter number = "))
i=1
while i<=n:
	j=1
	while j<=i:
		print(j,end="")
		j=j+1
	print()
	i=i+1

10.
1
22
333
4444
55555

n=int(input("Enter number = "))
i=1
while i<=n:
	j=1
	while j<=i:
		print(i,end="")
		j=j+1
	print()
	i=i+1

11.
A
AB
ABC
ABCD
ABCDE
n=int(input("Enter number = "))
i=1
while i<=n:
	j=1
	while j<=i:
		print(chr(64+j),end="")
		j=j+1
	print()
	i=i+1

12.
a
ab
abc
abcd
abcde

n=int(input("Enter number = "))
i=1
while i<=n:
	j=1
	while j<=i:
		print(chr(96+j),end="")
		j=j+1
	print()
	i=i+1

13.
1
01
101
0101
10101
n=int(input("Enter number = "))
i=1
while i<=n:
	j=1
	while j<=i:
		if i%2==0:
			if j%2!=0:
				print("0",end="")
			else:
				print("1",end="")
		else:
			if j%2!=0:
				print("1",end="")
			else:
				print("0",end="")
		j=j+1
	print()
	i=i+1

14.
1
23
456
78910
a=int(input("Enter Number = "))
i=1
k=1
while i<=a:
	j=1
	while j<=i:
		print(k,end="")
		k=k+1
		j=j+1
	print()
	i=i+1

15.
A
BB
CCC
DDDD
EEEEE
a=int(input("Enter Number = "))
i=1
while i<=a:
	j=1
	while j<=i:
		print(chr(64+i),end="")
		j=j+1
	print()
	i=i+1

16.
a
bc
def
ghij
klmno

n=int(input("Enter Number = "))
i=1
k=1
while i<=n:
	j=1
	while j<=i:
		print(chr(96+k),end=" ")
		k=k+1
		j=j+1
	print()
	i=i+1

17.
*
##
***
####
*****

a=int(input("Enter Number = "))
i=1
while i<=a:
	j=1
	while j<=i:
		if i%2!=0:
			print("*",end="")
		else:
			print("#",end="")
		j=j+1
	print()
	i=i+1

18.
1
10
101
1010
10101
a=int(input("Enter Number = "))
i=1
while i<=a:
	j=1
	while j<=i:
		if j%2!=0:
			print("1",end="")
		else:
			print("0",end="")
		j=j+1
	print()
	i=i+1

19.
*
* *
*   *
*     *
* * * * *

if i==j or j==1:
	if j%2==0:
		print("0",end=" ")

a=int(input("Enter Number = "))
i=1
while i<=a:
	j=1
	while j<=i:
		if i==j or j==1 or i==a:
			print("*",end=" ")
		else:
			print(" ",end=" ")
		j=j+1
	print()
	i=i+1


20.
1
12
1 3
1  4
12345

a=int(input("Enter Number = "))
i=1
while i<=a:
	j=1
	while j<=i:
		if i==j or j==1 or i==a:
			print(j,end=" ")
		else:
			print(" ",end=" ")
		j=j+1
	print()
	i=i+1


21.
1
22
3 3
4  4
55555

a=int(input("Enter Number = "))
i=1
while i<=a:
	j=1
	while j<=i:
		if i==j or j==1 or i==a:
			print(i,end=" ")
		else:
			print(" ",end=" ")
		j=j+1
	print()
	i=i+1

22.
A
AB
A C
A  D
ABCDE

a=int(input("Enter Number = "))
i=1
while i<=a:
	j=1
	ch=64
	while j<=i:
		if i==j or j==1 or i==a:
			print(chr(ch+j),end=" ")
		else:
			print(" ",end=" ")
		j=j+1
	print()
	i=i+1

23.
a
bc
d f
g  j
klmno

a=int(input("Enter Number = "))
i=1
ch=97
while i<=a:
	j=1
	while j<=i:
		if i==j or j==1 or i==a:
			print(chr(ch),end=" ")
		else:
			print(" ",end=" ")
		ch=ch+1
		j=j+1
	print()
	i=i+1

24.
*
**
*@*
*@@*
* * * * *
a=int(input("Enter Number = "))
i=1
while i<=a:
	j=1
	while j<=i:
		if i==j or j==1 or i==a:
			print("*",end=" ")
		else:
			print(chr(64),end=" ")
		j=j+1
	print()
	i=i+1

25.
5
54
543
5432
54321
a=int(input("Enter Number = "))
i=a
while i>=1:
	j=a
	while i<=j:
		print(j,end=" ")
		j=j-1
	print()
	i=i-1

26.
*
*#
*#*
*#*#
*#*#*

a=int(input("Enter Number = "))
for i in range(1,a+1):
	j=1
	while j<=i:
		if j%2==0:
			print("#",end=" ")
		else:
			print("*",end=" ")
		j=j+1
	print()

27.
1
10
1 1
1  0
10101

a=int(input("Enter Number = "))
i=1
while i<=a:
	j=1
	while j<=i:
		if i==j or i==a:
			if j%2==0:
				print("0",end=" ")
			else:
				print("1",end=" ")
			#print("1",end=" ")
		elif j==1:
			print("1",end=" ")
		else:
			print(" ",end=" ")
		j=j+1
	print()
	i=i+1

28.
1
123
12345
1234567
123456789

n=int(input("Enter Number = "))
i=1
while i<=n:
	j=1
	while j<=2*i-1:
		print(j,end=" ")
		j=j+1
	print()
	i=i+1

29.
1
222
33333
4444444
555555555

n=int(input("Enter Number = "))
i=1
while i<=n:
	j=1
	while j<=2*i-1:
		print(i,end=" ")
		j=j+1
	print()
	i=i+1

30.
***** 
**** 
***
**
* 

n=int(input("Enter Number = "))
i=1
while i<=n:
	j=n
	while j>=i:
		print("*",end=" ")
		j=j-1
	print()
	i=i+1
31.
12345
1234
123
12
1

n=int(input("Enter Number = "))
i=n
while i>=1:
	j=1
	while j<=i:
		print(j,end=" ")
		j=j+1
	print()
	i=i-1

32.
55555
4444
333
22
1

n=int(input("Enter Number = "))
i=5
while i>=1:
	j=1
	while j<=i:
		print(i,end=" ")
		j=j+1
	print()
	i=i-1

33.
ABCDE
ABCD
ABC
AB
A

n=int(input("Enter Number = "))
i=n
while i>=1:
	j=1
	while j<=i:
		print(chr(64+j),end=" ")
		j=j+1
	print()
	i=i-1

34.
EEEEE
DDDD
CCC
BB
A

n=int(input("Enter Number = "))
i=n
while i>=1:
	j=1
	while j<=i:
		print(chr(64+i),end=" ")
		j=j+1
	print()
	i=i-1

35.
*****
*  *
* *
**
*

n=int(input("Enter Number = "))
i=n
while i>=1:
	j=1
	while j<=i:
		if j==1 or i==j or i==n:
			print("*",end=" ")
		else:
			print(" ",end=" ")
		j=j+1
	print()
	i=i-1

36.
ABCDE
A  D
A C
AB
A

n=int(input("Enter Number = "))
i=n
while i>=1:
	j=1
	while j<=i:
		if j==1 or j==i or i==n:
			print(chr(64+j),end=" ")
		else:
			print(" ",end=" ")
		j=j+1
	print()
	i=i-1

37.
*****
####
***
##
*

n=int(input("Enter Number = "))
for i in range(n,0,-1):
	for j in range(1,i+1):
		if i%2!=0:
			print("*",end="")
		else:
			print("#",end="")
	print()

38.
55555
4  4
3 3
22
1

n=int(input("Enter Number = "))
for i in range(n,0,-1):
	for j in range(1,i+1):
		if j==1 or j==i or i==n:
			print(i,end=" ")
		else:
			print(" ",end=" ")
	print()

**39.
123456
54321
1234
321
12
1

n=int(input("Enter Number = "))
for i in range(n,0,-1):
	for j in range(1,i+1):
		if i%2!=0:
			print(j,end="")
		else:
			print(j,end="")
		j=j+1
	print()


**40.
*
**
****
********
***********

n=int(input("Enter Number = "))
i=1
l=1
while i<=n:
	j=i
	while j<=l:
		print("*",end=" ")
		#print(l)
		j=j+1
	l+=i+1
	print()
	i=i+1

41.
A
BCD
EFGHI
JKLMNOP

n=int(input("Enter number = "))
i=1
j=1
while i<=n:
	while j<=i:
		print(chr(64+j),end=" ")
		j=j+1
	print()
	i=i+2

42.
54321
5432
543
54
5

n=int(input("Enter number = "))
i=1
while i<=n:
	j=n
	while j>=i:
		print(j,end=" ")
		j=j-1
	print()
	i=i+1

43.
    1
   12
  123
 1234
12345

n=int(input("Enter number = "))
i=1
while i<=n:
	j=1
	while j<=n-i:
		print(" ",end=" ")
		j=j+1
	a=1
	while a<=i:
		print(a,end=" ")
		a=a+1
	print()
	i=i+1

44.
    1
   22
  333
 4444
55555

n=int(input("Enter number = "))
i=1
while i<=n:
	j=1
	while j<=n-i:
		print(" ",end=" ")
		j=j+1
	a=1
	while a<=i:
		print(i,end=" ")
		a=a+1
	print()
	i=i+1


45.
    5
   44
  333
 2222
11111

n=int(input("Enter number = "))
i=n
while i>=1:
	j=1
	while j<=i-1:
		print(" ",end=" ")
		j=j+1
	a=n
	while a>=i:
		print(i,end=" ")
		a=a-1
	print()
	i=i-1

46.
    A
   AB
  ABC
 ABCD
ABCDE

n=int(input("Enter number = "))
i=1
while i<=n:
	j=n
	while j>i:
		print(" ",end=" ")
		j=j-1
	a=1
	while a<=i:
		print(chr(64+a),end=" ")
		a=a+1
	print()
	i=i+1

47.
    1
   11
  1*1
 1**1
11111

n=int(input("Enter number = "))
i=1
while i<=n:
	j=n
	while j>i:
		print(" ",end=" ")
		j=j-1
	a=1
	while a<=i:
		if a==i or i==n or a==1:
			print("1",end=" ")
		else:
			print("*",end=" ")
		a=a+1
	print()
	i=i+1

48.
    A 
   AB
  A_C
 A__D
ABCDE

n=int(input("Enter number = "))
i=1
while i<=n:
	j=n
	while j>i:
		print(" ",end=" ")
		j=j-1
	a=1
	while a<=i:
		if a==i or a==1 or i==n:
			print(chr(64+a),end=" ")
		else:
			print("_",end=" ")
		a=a+1
	print()
	i=i+1


49.
    1
   10
  101
 1010
10101

n=int(input("enter number = "))
i=1
while i<=n:
	j=n
	while j>i:
		print(" ",end=" ")
		j=j-1
	s=1
	while s<=i:
		if s%2==0:
			print("0",end=" ")
		else:
			print("1",end=" ")
		s=s+1 
	print()
	i=i+1
	
50.
12345
 1234
  123
   12
    1

n=int(input("Enter Number = "))
i=n
while i>=1:
	a=n-1
	while a>=i:
		print(" ",end=" ")
		a=a-1
	j=1
	while j<=i:
		print(j,end=" ")
		j=j+1
	print()
	i=i-1

51.
55555
 4444
  333
   22
    1

n=int(input("Enter Number = "))
i=n
while i>=1:
	a=n-1
	while a>=i:
		print(" ",end=" ")
		a=a-1
	j=1
	while j<=i:
		print(i,end=" ")
		j=j+1
	print()
	i=i-1

52.
1 2 3 4 5
  1     4
    1   3
      1 2
        1
n=int(input("Enter Number = "))
i=n
while i>=1:
	a=n-1
	while a>=i:
		print(" ",end=" ")
		a=a-1
	j=1
	while j<=i:
		if j==i or j==1 or i==n:
			print(j,end=" ")
		else:
			print("_",end=" ")
		j=j+1
	print()
	i=i-1

53.
5 5 5 5 5
  4     4
    3   3
      2 2
        1
n=int(input("Enter Number = "))
i=n
while i>=1:
	j=n-1
	while j>=i:
		print(" ",end=" ")
		j=j-1
	s=1
	while s<=i:
		if s==i or s==1 or i==n:
			print(i,end=" ")
		else:
			print("_",end=" ")
		s=s+1
	print()
	i=i-1

54.
A B C D E
  A     D
    A   C
      A B
        A

n=int(input("Enter Number = "))
i=n
while i>=1:
	a=n-1
	while a>=i:
		print(" ",end=" ")
		a=a-1
	j=1
	while j<=i:
		if j==i or j==1 or i==n:
			print(chr(64+j),end=" ")
		else:
			print("_",end=" ")
		j=j+1
	print()
	i=i-1

55.
A B C D E
  A B C D
    A B C
      A B
        A

n=int(input("Enter Number = "))
i=n
while i>=1:
	j=n-1
	while j>=i:
		print(" ",end=" ")
		j=j-1
	b=1
	while b<=i:
		print(chr(64+b),end=" ")
		b=b+1
	print()
	i=i-1

56.
1 1 1 1 1
  2 2 2 2
    3 3 3
      4 4
        5

n=int(input("Enter Number = "))
i=1
while i<=n:
	j=1
	while j<i:
		print(" ",end=" ")
		j=j+1
	b=5
	while b>=i:
		print(i,end=" ")
		b=b-1
	print()
	i=i+1

57.
    *
   * *
  * * *
 * * * *
* * * * *

n=int(input("Enter Number = "))
i=1
while i<=n:
	j=n-1
	while j>=i:
		print(" ",end=" ")
		j=j-1
	a=1
	while a<=i:
		print("* ",end=" ")
		a=a+1
	print()
	i=i+1


58.
    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5

n=int(input("Enter Number = "))
i=1
while i<=n:
	j=n-1
	while j>=i:
		print(" ",end="")
		j=j-1
	a=1
	while a<=i:
		print(a,"",end="")
		a=a+1
	print()
	i=i+1

59.
    A
   A B
  A B C
 A B C D
A B C D E

n=int(input("Enter Number = "))
i=1
while i<=n:
	j=n-1
	while j>=i:
		print(" ",end="")
		j=j-1
	a=1
	while a<=i:
		print(chr(64+a),"",end="")
		a=a+1
	print()
	i=i+1

60.
    X
   X X
  X   X
 X     X
X X X X X

n=int(input("Enter Number = "))
i=1
while i<=n:
	j=n-1
	while j>=i:
		print(" ",end="")
		j=j-1
	a=1
	while a<=i:
		if i==a or i==n or a==1:
			print("X ",end="")
		else:
			print("_",end=" ")
		a=a+1
	print()
	i=i+1

61.
    *
   ***
  *****
 *******
*********
n=int(input("Enter Number = "))
i=1
while i<=n:
	j=n
	while j>i:
		print(" ",end="")
		j=j-1
	a=1
	while a<=(i*2)-1:
		print("*",end="")
		a=a+1
	print()
	i=i+1

62.
    1
   123
  12345
 1234567
123456789

n=int(input("Enter Number = "))
i=1
while i<=n:
	j=n
	while j>i:
		print(" ",end="")
		j=j-1
	a=1
	while a<=(i*2)-1:
		print(a,end="")
		a=a+1
	print()
	i=i+1

63.
    A
   ABC
  ABCDE
 ABCDEFG
ABCDEFGHI

n=int(input("Enter Number = "))
i=1
while i<=n:
	j=n
	while j>i:
		print(" ",end="")
		j=j-1
	a=1
	while a<=(i*2)-1:
		print(chr(64+a),end="")
		a=a+1
	print()
	i=i+1

64.
       *
      *_*
     *___*
    *_____*
   *_______*
  *_________*
 *___________*
***************

n=int(input("Enter Number = "))
i=1
while i<=n:
	j=n
	while j>i:
		print(" ",end="")
		j=j-1
	a=1
	while a<=(i*2)-1:
		if a==1 or i==n or a==(i*2)-1:
			print("*",end="")
		else:
			print("_",end="")
		a=a+1
	print()
	i=i+1

65.
     1
    1 1
   1 2 1
  1 3 3 1
 1 4 6 4 1

import math
n=int(input("enter n: "))
i=0
while i<n:
      s=1
      while s<=n-i:
            print(" ",end="")
            s=s+1
      j=0
      while j<=i:
            num=int(math.factorial(i)/(math.factorial(j)*math.factorial(i-j)))
            print(num,end=" ")
            j=j+1
      print()
      i=i+1

66.
    1
   1*1
  1***1
 1*****1
111111111
n=int(input("Enter Number = "))
i=1
while i<=n:
	j=n
	while j>i:
		print(" ",end="")
		j=j-1
	a=1
	while a<=(i*2)-1:
		if a==1 or i==n or a==(i*2)-1:
			print("1",end="")
		else:
			print("*",end="")
		a=a+1
	print()
	i=i+1

67
    A
   B B
  C   C
 D     D
EEEEEEEEE

n=int(input("Enter Number = "))
i=1
while i<=n:
	j=n
	while j>i:
		print(" ",end="")
		j=j-1
	a=1
	while a<=(i*2)-1:
		if a==1 or i==n or a==(i*2)-1:
			print(chr(64+i),end="")
		else:
			print(" ",end="")
		a=a+1
	print()
	i=i+1

68.
    #
   *#*
  **#**
 ***#***
****#****

n=int(input("Enter Number = "))
i=1
while i<=n:
	j=n
	while j>i:
		print(" ",end="")
		j=j-1
	a=1
	while a<=(i*2)-1:
		if a==i:
			print("#",end="")
		else:
			print("*",end="")
		a=a+1
	print()
	i=i+1

69.
*********
 *******
  *****
   ***
    *

n=int(input("Enter Number = "))
i=n
while i>=1:
	j=n
	while j>i:
		print(" ",end="")
		j=j-1
	a=1
	while a<=(i*2)-1:
		print("*",end="")
		a=a+1
	print()
	i=i-1

70.
* * * * *
 * * * *
  * * *
   * *
    *

n=int(input("Enter Number = "))
i=n
while i>=1:
	j=n
	while j>i:
		print(" ",end="")
		j=j-1
	a=1
	while a<=i:
		print("* ",end="")
		a=a+1
	print()
	i=i-1

71.
123456789
 1234567
  12345
   123
    1

n=int(input("Enter Number = "))
i=n
while i>=1:
	j=n
	while j>i:
		print(" ",end="")
		j=j-1
	a=1
	while a<=i*2-1:
		print(a,end="")
		a=a+1
	print()
	i=i-1

72.
A B C D E
 A B C D
  A B C
   A B
    A

n=int(input("Enter Number = "))
i=n
while i>=1:
	j=n
	while j>i:
		print(" ",end="")
		j=j-1
	a=1
	while a<=i:
		print(chr(64+a),end=" ")
		a=a+1
	print()
	i=i-1

73.
5 5 5 5 5
 4 4 4 4
  3 3 3
   2 2
    1

n=int(input("Enter Number = "))
i=n
while i>=1:
	j=n
	while j>i:
		print(" ",end="")
		j=j-1
	a=1
	while a<=i:
		print(i,end=" ")
		a=a+1
	print()
	i=i-1

74.
123456789
 1     7
  1   5
   1 3
    1

n=int(input("Enter Number = "))
i=n
while i>=1:
	j=n
	while j>i:
		print(" ",end="")
		j=j-1
	a=1
	while a<=i*2-1:
		if a==1 or a==i*2-1 or i==n:
			print(a,end="")
		else:
			print(" ",end="")
		a=a+1
	print()
	i=i-1

75.
123456789
 1+++++7
  1+++5
   1+3
    1

n=int(input("Enter Number = "))
i=n
while i>=1:
	j=n
	while j>i:
		print(" ",end="")
		j=j-1
	a=1
	while a<=i*2-1:
		if a==1 or a==i*2-1 or i==n:
			print(a,end="")
		else:
			print("+",end="")
		a=a+1
	print()
	i=i-1

76.
*
**
***
****
***
**
*

n=int(input("Enter Number = "))
i=1
while i<=n:
	j=1
	while j<=i:
		print("*",end="")
		j=j+1
	print()
	i=i+1
s=n-1
while s>=1:
	j=s
	while j>=1:
		print("*",end="")
		j=j-1
	print()
	s=s-1	
77.
1
12
123
1234
123
12
1

n=int(input("Enter Number = "))
i=1
while i<=n:
	j=1
	while j<=i:
		print(j,end="")
		j=j+1
	print()
	i=i+1
a=n-1
while a>=1:
	j=1
	while j<=a:
		print(j,end="")
		j=j+1
	print()
	a=a-1


78.
   1
  12
 123
1234
 123
  12
   1

n=int(input("N = "))
i=1
while i<=n:
	j=n-1
	while j>=i:
		print(" ",end="")
		j=j-1
	j=1
	while j<=i:
		print(j,end="")
		j=j+1
	print()
	i=i+1
i=n-1
while i>=1:
	j=n-i
	while j>=1:
		print(" ",end="")
		j=j-1
	j=1
	while j<=i:
		print(j,end="")
		j=j+1
	print()
	i=i-1
	
79.
1
1 2
1   3
1     4
1   3
1 2
1
n=int(input("Enter Number = "))
i=1
while i<=n:
	j=1
	while j<=i:
		if j==i or j==1:
			print(j,end=" ")
		else:
			print(" ",end=" ")
		j=j+1
	print()
	i=i+1
a=n-1
while a>=1:
	j=1
	while j<=a:
		if j==a or j==1:
			print(j,end=" ")
		else:
			print(" ",end=" ")
		j=j+1
	print()
	a=a-1

80.
   *
  *_*
 *_*_*
*_*_*_*
 *_*_*
  *_*
   *

n=int(input("N = "))
i=1
while i<=n:
	j=n-1
	while j>=i:
		print(" ",end="")
		j=j-1
	s=1
	while s<=i*2-1:
		if s%2==0:
			print("_",end="")
		else:
			print("*",end="")
		s=s+1
	print()
	i=i+1
b=n-1
while b>=1:
	j=n-1
	while j>=b:
		print(" ",end="")
		j=j-1
	k=b*2-1
	while k>=1:
		if k%2==0:
			print("_",end="")
		else:
			print("*",end="")
		k=k-1
	print()
	b=b-1

81.
   *
  *_*
 *___*
*_____*
 *___*
  *_*
   *

n=int(input("N = "))
i=1
while i<=n:
	j=n-1
	while j>=i:
		print(" ",end="")
		j=j-1
	s=1
	while s<=i*2-1:
		if s==1 or s==i*2-1:
			print("*",end="")
		else:
			print("_",end="")
		s=s+1
	print()
	i=i+1
b=n-1
while b>=1:
	j=n-1
	while j>=b:
		print(" ",end="")
		j=j-1
	k=b*2-1
	while k>=1:
		if k==b*2-1 or k==1:
			print("*",end="")
		else:
			print("_",end="")
		k=k-1
	print()
	b=b-1

82.PENDING
n=int(input("N = "))
i=1
while i<=n:
	j=1
	while j<=n:
		if i==1 or i==n or j==n or j==1 or i==j or j==n-i or j==n-i:
			print(".",end=" ")
		else:
			print(" ",end=" ")
		j=j+1
	print()
	i=i+1

83.
    1
   212
  32123
 4321234
543212345

n=int(input("N = "))
i=1
while i<=n:
	j=n-i
	while j>=1:
		print(" ",end="")
		j=j-1
	a=i
	while a>=1:
		print(a,end="")
		a=a-1
	b=2
	while b<=i:
		print(b,end="")
		b=b+1
	print()
	i=i+1

84
*           *
**         **
***       ***
****     ****
*****   *****
****** ******

n=int(input("N = "))
i=0
while i<=n:
	j=0
	while j<=i:
		print("*",end="")
		j=j+1
	a=n
	while a>i:
		print(" ",end="")
		a=a-1
	j=0
	while j<=n-i:
		print(" ",end="")
		j=j+1
	a=0
	while a<=i:
		print("*",end="")
		a=a+1
	print()
	i+=1
85.
**********
****  ****
***    ***
**      **
*        *

n=int(input("N = "))
i=n
while i>=1:
	j=1
	while j<=i:
		print("*",end="")
		j=j+1
	a=n
	while a>i:
		print(" ",end="")
		a=a-1
	a=n-1
	while a>=i:
		print(" ",end="")
		a=a-1
	j=1
	while j<=i:
		print("*",end="")
		j=j+1
	print()
	i=i-1
86.
'''
n=int(input("N = "))
i=n
while i>=1:
	j=1
	while j<=i:
		print("*",end="")
		j=j+1
	a=n
	while a>i:
		print(" ",end="")
		a=a-1
	a=n-1
	while a>=i:
		print(" ",end="")
		a=a-1
	j=1
	while j<=i:
		print("*",end="")
		j=j+1
	print()
	j=0
	while j<=i:
		print("*",end="")
		j=j+1
	a=n
	while a>i:
		print(" ",end="")
		a=a-1
	j=0
	while j<=n-i:
		print(" ",end="")
		j=j+1
	a=0
	while a<=i:
		print("*",end="")
		a=a+1
	print()
	i+=1
'''
89.
    1
   101
  10101
 1010101
101010101

n=int(input("N = "))
i=1
while i<=n:
	j=n
	while j>i:
		print(" ",end="")
		j=j-1
	a=1
	while a<=(i*2)-1:
		if a%2==0:
			print("0",end="")
		else:
			print("1",end="")
		a=a+1
	print()
	i=i+1
'''

