print("Student Marks Analysis")
num1,num2,num3,num4,num5=map(int,input("Enter Marks of five subject separated by commas=").split(","))
Total=num1+num2+num3+num4+num5
Average=Total/5
percentage=((Total/500)*100)
print("Total={}".format(Total))
print("Average=",Average)
print(f"Percentage={percentage}%")