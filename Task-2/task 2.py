def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Invalid operation (division by zero)"

print("Simple Calculator")
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

ch=input("Enter choice (1/2/3/4): ")
a=float(input("Enter first number: "))
b=float(input("Enter second number: "))

if ch=="1":
    print("Result is",add(a,b))
elif ch=="2":
    print("Result is",sub(a,b))
elif ch=="3":
    print("Result is",mul(a,b))
elif ch=="4":
    print("Result is",div(a,b))
else:
    print("Invalid choice")
