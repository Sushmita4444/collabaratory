def divide(a,b):
    if(b==0):
        print("division by zero error")
    return a/b
x=float(input("Enter number 1"))
y=float(input("Enter number 2"))
print("division is: ",divide(x,y))
