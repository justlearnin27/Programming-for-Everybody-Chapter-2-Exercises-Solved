#Chapter 4 Exercise 6
#Defined a function adding an if and else statement
def computepay(hours,rate):
    if hours > 40:
        pay = 40 * rate + ((hours - 40) * 1.5 * rate)
    else:
        pay = hours * rate
    return pay
#Input statement for hours and pay
hours = int(input("enter hours: "))
rate = float(input("enter rate: "))
#Function is ready
x = computepay(hours,rate)
print(x);


#CHapter 4 Exercise 7
#Defined a function with if and elif and returning the inner function value
def computegrade(score):
    if score > 0.0 and score < 1.0:
        if score >= 0.9:
            return'A'
        elif score >= 0.8:
            return'B'
        elif score >= 0.7:
            return'C'
        elif score >= 0.6:
            return'D'
        else:
            return'F'
    else:
        return "bad score"
#try and except like the last Chapter
try:
    score = float(input('Enter your score'))
except:
    print("bad score")
    quit()
#function is ready computegrade
x = computegrade(score)
print(x);
