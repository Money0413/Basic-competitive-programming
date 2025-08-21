A = int(input("enter a number"))

reverse=0
while A > 0:
    digit = A % 10
    reverse = reverse * 10 + digit
    A = A // 10

print(reverse )'''


#11. Take a number A as input, print its multiplication table having the first 10 multiples. 
#Input:-3 
#Output:- 
#3 * 1 = 3 
#3 * 2 = 6 
#3 * 3 = 9 
#3 * 4 = 12 
#3 * 5 = 15 
#3 * 6 = 18 
#3 * 7 = 21 
#3 * 8 = 24 
#3 * 9 = 27 
#3 * 10 = 30

''A = int(input("enter a number"))

i = 1

while i <= 10:
    print(A, "*", i," =", A * i)
    i = i + 1'''


#12. You are given two integers A and B. You have to find the value of A^B. 
#Input:- A = 2 , B = 3 
#Output:- 8 
#Explaination:- For A=2 and B=3, the value of 2^3 = 2 * 2 * 2 = 8.

'''A = int(input("Enter a number "))
B = int(input("Enter a number "))

count=1

i = 1

while i <= B:
    count = count * A
    i = i + 1

print("count:", count)'''
