print("======================simple ticket calculator========================")

ticket1=int(input("enter the ticket1:"))
operator=(input("enter the operator(+,-,*,/)"))
ticket2=int(input("enter the ticket2:"))


if operator=="+":
    result=ticket1+ticket2
elif operator=="-":
    result=ticket1-ticket2
elif operator=="*":
    result=ticket1*ticket2
elif operator=="/":
    result=ticket1/ticket2

else:
    print("invalid ")

print(f"result :{result}")



print("========================================")