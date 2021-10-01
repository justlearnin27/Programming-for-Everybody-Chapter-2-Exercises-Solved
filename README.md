# Programming-for-Everybody-Chapter-Exercises-Solved
Solutions for Chapter 2  Exercises 
#Excercise 2
nam = input("Enter your name: ")
print('Welcome ' , nam )

#Excercise 3
hr = input('Enter hours: \n')
rate = input('Enter rate: \n')
pay = hr * rate
print(pay)

#Exercise 4
width = 17
height = 12.0
w = width//2
x = width/2.0
y = height/3
z = 1 + 2 * 5
print(w)
print(x)
print(y)
print(z)

#Exercise 5
temp = float(input("Enter body temp in C:"))
cvt = ((temp * 9) / 5) + 32
print(cvt)

Solutions for Chapter 3 Exercises
#Excercise 1
hrs  = input("Enter hours :")
rate = input("Enter rate :")
if hrs > 40:
    pay = 40 * rate + (1.5 * rate * (hrs - 40))
else:
    pay = hrs * rate
print(float(pay));

#Exercise 2
try:
    hrs = int(input("Enter hours :"))
    rate = float(input("Enter rate :"))
except:
    print('Error, please enter numeric input');
    quit()
hrs = input("Enter hours :")
rate = input("Enter rate :")
if hrs > 40:
    pay = 40 * rate + (1.5 * rate * (hrs - 40))
else:
    pay = hrs * rate
print(float(pay));

#Exercise 3
try:
    fn = input('Enter your score')
except:
    print("bad score")
if fn > 0.0 and fn < 1.0:
    if fn >= 0.9:
        print(A)
    elif fn >= 0.8:
        print(B)
    elif fn >= 0.7:
        print(C)
    elif fn >= 0.6:
        print(D)
    else fn < 0.6:
        print(F)
else:
    print("Bad score")
