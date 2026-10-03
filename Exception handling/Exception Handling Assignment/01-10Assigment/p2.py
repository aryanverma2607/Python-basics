'''Q2. EMAIL VALIDATION USING CUSTOM EXCEPTIONS
A company wants to validate email addresses before creating user accounts.
Create the following custom exception classes:
1. DotException
2. AtTheRateException
3. DomainException
Requirements:
1. Create all three custom exceptions by inheriting from Exception.
2. Accept an email address from the user.
3. Validate the email according to the following rules.
Rules:
Rule 1:
The email must contain exactly one '@' character.
If this rule fails, raise:
AtTheRateException: Invalid @ usage
Rule 2:
The email must contain a '.' character after '@'.
If this rule fails, raise:
DotException: Invalid Dot usage
Rule 3:
The email must end with one of the following valid domains:
in
com
net
biz
If this rule fails, raise:
DomainException: Invalid Domain
4. Handle the exceptions using try-except.
5. If all conditions are satisfied, display:
Valid email address
6. Otherwise display the appropriate exception message followed by:
Invalid email address
## Sample Input 1:
[sample@gmail.com](mailto:sample@gmail.com)
## Sample Output 1:
Valid email address
## Sample Input 2:
[sample@gmail.com](mailto:sample@gmail.com).
## Sample Output 2:
DotException: Invalid Dot usage
Invalid email address
## Sample Input 3:
sample@[g@mail.com](mailto:g@mail.com)
## Sample Output 3:
AtTheRateException: Invalid @ usage
Invalid email address
## Sample Input 4:
[sample@gmail.con](mailto:sample@gmail.con)
## Sample Output 4:
DomainException: Invalid Domain
Invalid email address
## Additional Test Cases:
student@gmail
studentgmail.com
student@@gmail.com
[student@gmail.xyz](mailto:student@gmail.xyz)
[student@gmail.net](mailto:student@gmail.net)
'''
class DotException(Exception):
    pass
class AtTheRateException(Exception):
    pass
class DomainException(Exception):
    pass

def check(email):
    def check_AtTheRate(email):
        if email.count("@") != 1:
            raise AtTheRateException("Invalid @ usage")

    def check_Dot(email):
        if email.count(".") != 1:
            raise DotException("Invalid '.' usage")

    def check_Domain(email):
        # index = email.index(".")
        # mail = email[index+1:len(email)+1]
        # if mail != "in" and mail != "com" and mail != "net" and mail != "biz":
        #     raise DomainException("Invalid Domain")
        if email.endswith(".com") or email.endswith(".in") or email.endswith(".net") or email.endswith(".biz") :
            pass
        else:
            raise DomainException("Invalid Domain")
    check_AtTheRate(email)
    check_Dot(email)
    check_Domain(email)

email = input("Enter Email ID: ")
try:
    check(email)
except DotException as e:
    print("DotException :",e)
except AtTheRateException as e:
    print("AtTheRateException :",e)
except DomainException as e:
    print("DomainException :",e)
else:
    print("Valid Email Address")
