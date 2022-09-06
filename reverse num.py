def reverse(num):
    reversed_num = ""
    for i in num:
        reversed_num = i+reversed_num
    print("reversed num is:",reversed_num)

num = input("enter a num:")
print("entered num",num)
reverse(num)
