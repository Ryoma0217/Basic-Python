a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO
a = input("aの値を入力: ")
b = input("bの値を入力: ")
x = int(a)
for i in range(2,x):
  if (x%i==0):
    print("これは素数ではありません")
    break
else:
    print("これは素数です")
y = int(b)
for i in range(2,y):
  if (y%i==0):
    print("これは素数ではありません")
    break
else:
    print("これは素数です")