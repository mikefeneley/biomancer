#print("To numerically investigate the limit of a sequence, I referenced a function that returns the nth element of the sequence:")
#print("t_0 = sqrt(1+0)")
#print("t_1 = sqrt(1+1)")
#print("t_2 = sqrt(1+2)")
#print("t_3 = sqrt(1+2*sqrt(1+3))")
#print("t_4 = sqrt(1+2*sqrt(1+3*sqrt(1+4)))")
#print("t_5 = sqrt(1+2*sqrt(1+3*sqrt(1+4*sqrt(1+5))))")
#print("etc.")

import math

def ramanujan_sqrt_sequence(n):
 
 if n == 1:
  t_n = math.sqrt(2)
 else:
  t_n = 1

 for i in range(n,1,-1):
  t_n = math.sqrt((i*t_n)+1)
 print(t_n) 

n = int(input("The nth element of your sequence is:"))
print(ramanujan_sqrt_sequence(n))
print("As n goes to infinity, the value of the nth element of the sequence will tend to 3.")
