a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO
x = int(a)
y = int(b)
while y!=0 :
  z = x%y
  x = y
  y = z

  if y == 0:
     print(x)