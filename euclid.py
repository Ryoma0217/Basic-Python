def euclid(a,b):
  x = int(a)
  y = int(b)
  while y!=0 :
   z = x%y
   x = y
   y = z

   if y == 0:
    return int(x)

    if (x==1 and y==0):
    return True
  else:
    return False