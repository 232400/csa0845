def maximum(a, b, c) :
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

a = input("enter 1st number\n")
b = input("enter 2nd number\n")
c = input("enter 3rd number\n")
print(maximum(a, b, c))
