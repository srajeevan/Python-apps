
import re
txt_name = input("Enter your name:")
chk_name = re.findall("[a-zA-Z]", txt_name)
if len(chk_name) < 1:
    txt_name = input("Enter a valid name:")
txt_age = input("Enter your age:")
txt_phone = input("Enter your phone number:")


print("Age:"+txt_age)
print("Phone NUmber:"+txt_phone)