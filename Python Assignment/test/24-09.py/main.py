from string_operation import substring
from list_operation import l_op
while True:
    print("""========== MENU ==========

1. Print All Substrings
2. Minimum Size Subarray Sum
3. Exit""")
    choice=int(input("Enter Your Choice:"))
    match choice:
        case 1:
            x=input("Enter String: ")
            substring(x)
        case 2:
            number=int(input("Enter Size of Array: "))
            target=int(input("Enter target: "))
            l=[]
            for i in range(number):
                x=int(input(f"Enter Element {i+1} of list1:"))
                l.append(x)
            print("Minimum size subarray: ",l_op(l,target))
        case 3:
            print("Thank you for using the application.")
            break
        case __:
            print("Invalid Case")