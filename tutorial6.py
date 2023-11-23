# Student Number 00000000

# Define function
def f(x):
    return(-x**2+3*x-2)


# Print table of values
print(" # # # f(x) = -x^2 + 3x - 2 from a=1 to b=2 # # # ")
x = 1.0
middlesum = 0.0
while x < 2.01:
    print("When x =",x,"=> f(x) =", f(x))
    middlesum += f(x)
    x += 0.10


# Compute first, last and middle sum
first = f(1)
last = f(2)
middlesum -= first
middlesum -= last


# Results of Trapezium Rule with error
h = 0.10
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
