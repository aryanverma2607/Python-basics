import webbrowser


print("1. Google")
print("2. youtube")
print("3. linkedin")

x=int(input("Enter choice: "))
if x==1:
    webbrowser.open("https://www.google.com")
elif x==2:
    webbrowser.open_new("https://www.youtube.com")
elif x==3:
    webbrowser.open_new_tab("https://www.linkedin.com")
else:
    print("Incorrect choice")
