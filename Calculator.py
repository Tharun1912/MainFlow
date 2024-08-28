a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

ch = int(input("Enter choice (1/2/3/4): "))

def calculator(a, b, ch):
    if ch == 1:
        return a + b
    elif ch == 2:
        return a - b
    elif ch == 3:
        return a * b
    elif ch == 4:
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operation"

result = calculator(a, b, ch)
print("The result is:", result)
