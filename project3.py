a=int(input("Enter the first number:"))
b=int(input("Enter the first number:"))
c=int(input("Enter the first number:"))

big=a
if big<b:
    big=b
if big<c:
    big=c
print("biggest is: ",big)