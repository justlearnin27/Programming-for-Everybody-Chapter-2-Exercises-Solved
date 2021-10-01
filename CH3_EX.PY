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
