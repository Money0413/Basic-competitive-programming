A=int(input("enter a number"))
B=int(input("enter a number"))
C=int(input("enter a number"))
if A < B and A < C:
    print("The minimum number is:", A)
elif B < A and B < C:
    print("The minimum number is:", B)
else:
    print("The minimum number is:", C)