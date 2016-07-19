#2

def cube(num):
  return num * num * num

def avg(a,b,c,d):
  return (a + b + c + d) / 4

def triplicate(text):
  return text + text + text

def multiplicate(text,number):
  return text * number

#3

def extract_root(a,b,c):
  a = int(str(a))
  b = int(str(b))
  c = int(str(c))
  y1 = (- b + (b ** 2 - 4 * a * c) ** (1/2)) / (2 * a)
  y2 = (- b - (b ** 2 - 4 * a * c) ** (1/2)) / (2 * a)
  return "the solutions is" + str(y1) + "," + str(y2)
