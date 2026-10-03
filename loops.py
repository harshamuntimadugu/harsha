n=int(input("enter n:"))
even_count=0
odd_count=0
for i  in range (1,n+1):
    if i%2==0:
        even_count=+1
    else:
        odd_count=+1
print(f"even numbers:{even_count}")
print(f"odd numbers:{odd_count}")




print("==================digital locker==============")

num=int(input("enter number:"))
temp=abs(num)
count=0

if temp==0:
    count+=1
else:
    while temp>0:
        temp=temp//10
        count+=1
print(f"number of digits:{count}")





balance=10000
while balance>0:
    amount=int(input("enter the withdrawal amount:"))
    if amount<=0:
        print("invalid amount")
        continue
    if amount >balance:
        print("insufficient balance")
        continue
    balance=amount
    print(f"remaining balance:{balance}")
print("account balance empty.session ended.")




print("======================guess the number================")

identify=10

while True:
    guess=int(input("guess:"))
    if guess<identify:
        print("too low")
    elif guess >identify:
        print("too high")
    else:
        print("correct")

