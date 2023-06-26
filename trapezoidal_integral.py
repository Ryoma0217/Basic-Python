from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------
import math
a = 0
b = math.pi/2
N = 100
h = (b-a)/N

S = (h/2)*sum((sin((a+(i-1)*h))+sin((a+i*h)))for i in range (1,N+1))
print(S)