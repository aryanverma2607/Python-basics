'''
9. Happy Number List Analyzer

Scenario
Store numbers in a list and identify Happy Numbers.

A number is called Happy if repeatedly replacing it by the sum of squares of its digits eventually becomes 1.

Example
19

1² + 9² = 82

8² + 2² = 68

6² + 8² = 100

1² + 0² + 0² = 1

Therefore, 19 is a Happy Number.

Another Example

7

7² = 49

4² + 9² = 97

9² + 7² = 130

1² + 3² + 0² = 10

1² + 0² = 1

Therefore, 7 is a Happy Number.

Non-Happy Number Example

4

4² = 16

1² + 6² = 37

3² + 7² = 58

5² + 8² = 89

8² + 9² = 145

1² + 4² + 5² = 42

4² + 2² = 20

2² + 0² = 4

Again 4 appears and the cycle repeats.

Therefore, 4 is NOT a Happy Number.

Requirements

* Read N and list elements from user
* Find all Happy Numbers
* Store Happy Numbers in another list
* Count Happy Numbers
* Find Largest Happy Number
* Display Happy Number List

Test Case 1

Input:
[19, 7, 4, 20]

Output:
Happy Numbers = [19, 7]
Count = 2
Largest Happy Number = 19

Test Case 2

Input:
[13, 10, 4]

Output:
Happy Numbers = [13, 10]
Count = 2
Largest Happy Number = 13

Test Case 3

Input:
[2, 3, 4]

Output:
Happy Numbers = []
Count = 0
Largest Happy Number = Not Available
'''

n = int(input("Enter size: "))
arr = []

for i in range(n):
    x = int(input(f"Enter number {i+1}: "))
    arr.append(x)
print("\nInput:", arr)

happy = []
for ch in arr:
    a = ch
    visited = []
    while ch != 1 and ch not in visited:
        visited.append(ch)
        sum = 0
        while ch > 0:
            rem = ch % 10
            sum += rem*rem
            ch = ch // 10
        ch = sum
    if ch == 1:
        happy.append(a)
print("Happy Numbers:",happy)
print("Count:",len(happy))

if len(happy) > 0:
    print("Largest Happy Number:",max(happy))
else:
    print("Largest Happy Number: Not Available")





