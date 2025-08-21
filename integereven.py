A = int(input("Enter a positive integer: "))

count = 0
i = 2

while i <= A:
    count += i
    i += 2

print("Sum of even numbers:", count)