# Student Number 00000000

# Define function
def f(x):
    return(-x**2+3*x-2)

# h, a and b
h = 0.10
a = 1
b = 2

# Print table of values
print(" # # # f(x) = -x^2 + 3x - 2 from a=1 to b=2 # # # ")
x = a
while x < b+h/2:
    print("When x =",x,"=> f(x) =", f(x))
    x += h


# Compute first, last and middle sum
first = f(a)
last = f(b)
x = a+h # Don't start at a=1, start at 1.1
middlesum = 0
while x < b: # finish at 1.9
    middlesum += f(x)
    x += h


# Results of Trapezium Rule with error
ApproxValue = (h/2)*(first + 2*middlesum + last)
TrueValue = 1/6

print(" # # # Example of Trapezium Rule Values # # # ")
print("First Height:", first)
print("Last Height:", last)
print("Middle Sum:", middlesum)
print("Integration is approximately", ApproxValue)
print("True value of integration is 1/6")
error = 100*(TrueValue-ApproxValue)/TrueValue
print("Therefore the error is ",error,"%")

# QUIT
quit()
