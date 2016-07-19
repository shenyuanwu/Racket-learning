##3.
def flop_flip(pangram=str):
  """return short half number plus longer half number
  str -> str"""
  if len(str) % 2 ==0:
    return pangram[len(str):]+pangram[0:len(str)]

        
##6.
#a.
def collatz(num):
  """returns the number of odd or even of "num"

  num -> num"""
  if num % 2 == 0:
    return num /2
  else:
    return 1 + 3 * num
