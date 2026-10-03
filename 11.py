shopping_amount=int(input("enter the shopping_amount:"))
day_of_week=input("enter the day:")

if shopping_amount >1000 or day_of_week=="sunday":
    print("discount avaliable")

else:
    print("no discount ")


print("==============================")


user_name=input("enter the user_name:")
password=input("enter the password: ")

if user_name =="harsha" and password=="harsha@123":
    print("access denied")

else:
    print("accaes not found")


print("============================")

import calendar
year=int (input("enter the year:"))
month=int(input("enter the month:"))

print("/n",calendar.month(year,month))



print("==========================================")
college_name=input("enter the college_name:")
user_name=input("enter the user_name")

if college_name=="joyuniversity":
    print("correct college")

else:
    print("wrong college")


print("==================")

product_price = int(input("Enter the product price: "))
is_verified = input("Is verified (yes/no): ").lower()

if product_price > 0 and is_verified == "yes":
    print("verified")
else:
    print("not_verified")
