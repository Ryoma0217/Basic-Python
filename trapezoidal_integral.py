from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------
import math
def integral (f,a=0,b=1,n=100):
  h = (b-a)/n
  S = 0
  for i in range (1,n+1):
    f1 = f(a+(i-1)*h)
    f2 = f(a+i*h)
    S += h*(f1+f2)/2
    return float(S)
result1 = integral(sin,0,math.pi/2,50)
result1

def f(x):
  return 4/(1+x**4)
result2 = integral(f,a=0,b=1,n=100)
result2
 
def f(x):
  return (math.sqrt(math.pi))*(math.exp(-x**2))
result3 = integral(f,a=-100,b=100,n=1000)
result3