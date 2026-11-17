
while True:
    print("1. ADD two numbers")
    print("2.check even or odd")
    print("3 find square")
    print("4 EXIT")
    choice=int(input("enter choice"))
    match choice:
        case 1:
             a=int(input("enter first"))
             b=int(input("enter second number"))
             print("result",a+b)
        case 2:
              n= int(input("enter the number"))
              if n%2==0:
                  print("even")
              else:
                  print("odd ")
        case 4:
             print("EXIT.....")
             break
  
    again=input("Do you want to continue(yes/no)").lower()
    match again:
         case "yes":
               continue
         case "no":
               break
         case __:
                print("kuch bhi")
                break
print("Thanks")