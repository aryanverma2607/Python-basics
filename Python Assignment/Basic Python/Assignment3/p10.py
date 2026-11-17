print("Percentage Calculator")
total_marks,obtained_marks=map(int,input("Enter Total marks and Obtained marks:").split())
percentage=(obtained_marks/total_marks)*100
print("Percentage={}".format(percentage))