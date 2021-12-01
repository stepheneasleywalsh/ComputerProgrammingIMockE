# Student Number 00000000

# Define function
def f(x):
    return(-x**2+3*x-2)

# Print table of values
print(" # # # f(x) = -x^2 + 3x + 2 from a=1 to b=2 # # # ")
x = 1
sum = 0
while x < 2.05:
    print("When x =",round(x,4),"=> f(x) =", round(f(x),4))
    sum += f(x)
    x += 0.05

# Compute first, last and middle sum
first = f(1)
last = f(2)
sum -= first
sum -= last

h = 0.05
T = (h/2)*(first + 2*sum + last)
I = 1/6

# Results of Trapezium Rule with error
print(" # # # Example of Trapezium Rule Values # # # ")
print("First Height:", first)
print("Last Height:", last)
print("Middle Sum:", sum)
print("Integration is approximately", T)
print("True value of integration is 1/6")
error = round(100*(I-T)/(T),2)
print("Therefore the error is ",error,"%")

# Input a b and n
print(" # # # Please input your required values for this function # # # ")
a = float(input("Input real value a: "))
b = float(input("Input real value b: "))
n = int(input("Input non-zero integer n: "))

# Calculate integration
x = a
h = (b-a)/n
sum = 0
while x < b+h:
    sum += f(x)
    x += h
sum -= f(a)+f(b)
sum *= 2
sum += f(a) + f(b)
sum *= h/2
print("Integration from",a,"to",b,"is approximately",sum)

# QUIT
quit()