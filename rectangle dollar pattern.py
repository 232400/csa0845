rows = int(input("plase enter the total number of rows:"))
columns = int(input("please enter the total number of columns:"))

print("rectangle dollar pattern")
for i in range(rows):
    for i in range(columns):
        print('$', end = ' ')
    print()
