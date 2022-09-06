num1=input("enter num1:")
num2=input("enter num2:")
num3=input("enter num3:")
print("the greatest number is")
max=0
if num1>=num2 and num1>=num3:
    print(num1)
elif num2>=num1 and num2>=num3:
    print(num2)
else:    
    print(num3)
