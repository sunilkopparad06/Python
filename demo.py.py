a = int(input("enter the number: "))
if a%2 == 0:  
       	print("the given number is even number ")
else:
	print("given number is odd number: ")
num=int(input("Enter number to find the Factorial... "))


def fact(num):
    if num==1 or num==0:
        return 1
    else:
        return num * fact(num-1)
print("Factorial Number of",num,"is :",fact(num))      


def reverse_string(input_string):
    return input_string[::-1]
result = reverse_string("Skyllx")
print(result)


def largest_of_three(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
result = largest_of_three(10, 25, 15)
print(result)


def is_palindrome(input_string):
    return input_string == input_string[::-1]
input_str = "madam"
if is_palindrome(input_str):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


def merge_dicts(dict1, dict2):
    return dict1 | dict2
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = merge_dicts(dict1, dict2)
print(merged_dict)


import logging
class invalidcustomerror (Exception):
    pass
info_logger=logging.grtloggers("info")
debug_logger=logging.getlogger("debug")
error_logger=logging.getlogger("error")

info_logger=logging.setlevel(logging.info)
debug_logger=logging.setlevel(logging.debug)
error_logger=logging.setlevel(logging.error)

info_logger.fileHandler("info.txt")
debug_logger.fileHandler("debug.txt")
error_logger.fileHandler("error.txt")

info_logger.addHandler("info.file")
debug_logger.addHandler("debug.file")
error_logger.addHandler("error.file")

class invalidcustomerror (Exception):
    pass
acc_no=1234
password=2106
ac=0
pw=0
def accout():
    global ac
    global pw
    ac=(input("Enter the account number: "))zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
    pw=(input("Enter the password:: "))
    
    def verify():
        if acc_no==ac and password==pw:
            print("Login succesfully")
        else
            raise invalidcustomererror("please try to provide vailed ")

