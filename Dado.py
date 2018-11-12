import math
import random


estrazione = input('Inserisci numero estrazione : ')
estrazione=int(estrazione)
i=0
numeri=[0,0,0,0,0,0]
while i < estrazione :  
  num=random.randrange(1,7)
  numeri[num-1]+=1
  i += 1
  print(num)
  
print(numeri)