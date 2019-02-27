strs=input("enter string")
letters=0
digits=0
for c in strs:
    if c.isdigit():
        digits = digits + 1
    else:
        letters=letters + 1

print ("letter",letters)
print ("digits",digits)