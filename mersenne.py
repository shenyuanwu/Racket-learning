#a.

def mersenne(n):
  return 2 ** n - 1

#b.

print("write three number here and I will tell you the mersenne number of it")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
Ma = 2 ** a - 1
Mb = 2 ** b - 1
Mc = 2 ** c - 1
print("Your Mersenne numbers are " + str(Ma) + ", " + str(Mb) + "and " + str(Mc))
