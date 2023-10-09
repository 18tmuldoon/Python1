import random
#1
num = int(input("Input a Number"))

def count(num):
    x = num
    z = 1
    while x > 0:
        print (z)
        x = x-1
        z = z+ 1
        
count(num)

#2
print("1) Addition", "\n", "2) Subtraction")
imp = int(input("Enter 1 or 2:"))

if imp == 1:
    def add1():
        num1 = random.randint(5,20)
        num2 = random.randint(5,20)
        print( num1, " + ", num2)
        usrAns = int(input("Whats the answer"))
        ans = num1 + num2
        print ("Actual answer is = ", ans)

add1()
elif imp == 2