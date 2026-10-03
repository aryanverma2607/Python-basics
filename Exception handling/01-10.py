# try:
#     x=3
#     x.append(2)
#     print(x)
#     import xyz
#     file = open("corrrected.txt")
# except AttributeError:
#     print("Attribute Not found")
# except ImportError:
#     print("Please check module")
# except FileNotFoundError:
#     print("File Not Created")
# except (AttributeError,ImportError) as e:
#     print("Problem Occured : ",e)
# else:
#     print("Value of X is : ",x)
# finally:
#     print("Code")

# class DotException(Exception):
#     pass
# class AtTheRateException(Exception):
#     pass
# class DomainException(Exception):
#     pass

# def validate_email(email):
#     if email.count("@") !=1:
#         raise AtTheRateException("Invalid @ usage ")

# def validate_email(email):
#     if email.count(".") != 1:
#         raise DotException("Invalid . usage ")

# def validate_email(email):
#     mail=email.split(".")
#     if mail[1] != "com" or mail[1] != "org" or mail[1] != "in":
#         raise DomainException("Invalid Domain Usage ")
# email= input("Enter Your Mail ID:")
# try:
#     validate_email(email)
#     print("Valid Email")
# except AtTheRateException as e:
#     print("Problem Occured : ",e)
# except DotException as e:
#     print("Problem Occured : ",e)
# except DomainException as e:
#     print("Problem Occured : ",e)
