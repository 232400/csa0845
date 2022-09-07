s1= int(input("enter the marks of first student"))
s2= int(input("enter the marks of second student"))
s3= int(input("enter the marks of third student"))
s4= int(input("enter the marks of fourth student"))
s5= int(input("enter the marks of fifth student"))
if(s1>s2 and s1>s3 and s1>s4 and s1>s5):
    print("s1 is topper")
elif(s2>s1 and s2>s3 and s2>s4 and s2>s5):
    print("s2 is topper")
elif(s3>s1 and s3>s2 and s3>s4 and s3>s5):
    print("s3 is topper")
elif(s4>s1 and s4>s2 and s4>s3 and s4>s5):
    print("s4 is topper")
else:
    print("s5 is topper")
