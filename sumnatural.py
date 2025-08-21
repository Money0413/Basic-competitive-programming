N = int(input("Enter a positive integer: "))

count=0
i = 1


while i <= N:
    count += i
i += 1

print("Sum:" ,count)