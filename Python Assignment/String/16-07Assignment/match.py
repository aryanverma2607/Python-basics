'''
QNo 8:-- SMART TEXT PROCESSING SYSTEM

A software company is developing a Smart Text Processing System for
handling user messages. Different users require different text
transformations. To avoid creating separate applications, the company
wants a menu-driven program where users can select operations according
to their requirements.

The system should continue executing until the user selects Exit.

====================================================== MENU====================================================== 

===== Smart Text Processing System =====

1.  Reverse Complete String
2.  Reverse Every Word
3.  Reverse Word Order
4.  Exit

====================================================== Choice 1 ====================================================== 

Conditions: - Reverse the complete string - Ignore extra spaces - Keep
special characters (@,#,$,%) in their original positions - Do not use
built-in reverse functions

Example: Input: ja@va#py
         Output: yp@av#aj

Test Case 1: ab@cd#ef 
Output: fe@dc#ba

Test Case 2: py@th#on 
Output: no@ht#yp

Test Case 3: java@pro 
Output: orpa@vaj

====================================================== Choice 2 ====================================================== 

Conditions: - Reverse every word separately - Words containing digits
should not be reversed - Ignore extra spaces between words - First
letter of each reversed word should become uppercase

Example: Input: java is easy123 programming

Output: Avaj Si easy123 Gnimmargorp

Test Case 1: python full stack22 developer Output: Nohtyp Lluf stack22
Repoleved

Test Case 2: hello java99 world Output: Olleh java99 Dlrow

====================================================== Choice 3 ====================================================== 

Conditions: - Reverse order of words - Remove duplicate words - Ignore
case while checking duplicates - Keep only first occurrence

Example: Input: Java python Java react Python

Output: React Python Java

Test Case 1: HTML CSS HTML Java CSS Output: Java CSS HTML

Test Case 2: Python React Java Python React Output: Java React Python

====================================================== Choice 4 ======================================================

Program Closed Successfully
'''

while True:
     print("\n1.  Reverse Complete String")
     print("2.  Reverse Every Word")
     print("3.  Reverse Word Order")
     print("4.  Exit")
     ch = int(input("Enter your choice: "))
     match ch:
          case 1:
               ip = input("    Input : ") .lower()
               msg = ""
               i = 0
               while i<len(ip):

                    if ip[i] >= "a" and ip[i] <= "z" :
                         msg+= ip[i]
                    elif ip[i] == "@" or ip[i] == "#" or ip[i] == "%" or ip[i] == "$" :
                        msg += ip[i]
                    i += 1
               if len(msg) != len(ip):
                    print("\nMessage is:",msg)

               result = ""
               i = 0
               while i<len(msg):
                    if msg[i] >= "a" and msg[i] <= "z" :
                         result+= msg[i]
                    i += 1

               j = len(result)-1
               op = ""
               i = 0
               while i<len(msg):
                    if msg[i] == "@" or msg[i] == "#" or msg[i] == "%" or msg[i] == "$" :
                        op += msg[i]
                    else :
                         op += result[j]
                         j -= 1 
                    i+=1
               print("    Output:",op)

          case 2:
               msg = input("Input : ")
               result = ""
  
               i = 0
               while i<len(msg):
                    word=""
                    digit = 0
                    while i<len(msg) and msg[i] == " ":
                         i+=1
  
                    while i<len(msg) and msg[i] != " ":
                         if msg[i]>="0" and msg[i]<="9":
                             digit = 1
                         word += msg[i]
                         i+=1
  
                    if digit == 1:
                         result += word
                    else:
                      j = len(word) - 1
                      while j>=0:
                         if len(word) - 1 == j:
                              result+=word[j].upper()
                         else:
                              result+= word[j]
                         j-=1
                   
                    while i < len(msg) and msg[i] == " ":
                         i += 1

                    if i < len(msg):
                         result += " "
               
               print("Output:", result)
               
          case 3:
               msg = input("Input : ")
               result = ""
               fs = ""

               i = 0
               while i<len(msg):
                    word = ""
                    while i<len(msg) and msg[i] == " ":
                         i+=1

                    while i<len(msg) and msg[i] != " ":
                         word+= msg[i]
                         i+=1
                    
                    if word != "":
                         f1 = " "+word.lower()+" "
                         f2 = " "+fs.lower()+" "

                         if f1 not in f2:
                              if fs == "":
                                   fs = word
                              else:
                                   fs+=" "+word
                         
               result = ""

               i = len(fs) - 1

               while i >= 0:
                    temp = ""
          
                    while i >= 0 and fs[i] == " ":
                         i -= 1
          
                    while i >= 0 and fs[i] != " ":
                         temp = fs[i] + temp
                         i -= 1
          
                    if temp != "":
                         new = ""
                         j = 0
                         while j < len(temp):
                              if j == 0:
                                   new += temp[j].upper()
                              else:
                                   new += temp[j]
                              j += 1
                    
                         temp = new
               
                    if result == "":
                         result = temp
                    else:
                         result += " " + temp
               
               print("Output:", result)

          case 4:
               print("Program Closed Successfully")
               break
          case _:
               print("Invalid Input")