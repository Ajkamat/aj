num=int(input("enter a number"))
total=0
while(num>0):
    rem=num%10
    total=total+rem
    num=num//10
print("sum is ",total)