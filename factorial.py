import random
import time

#Section to create and store 100 random integers
numfile = open("Random_integer.txt", "w")
for i in range(100):
    line = str(random.randint(1,100)) + '\n'
    numfile.write(line)    
numfile.close()
id=random.randint(2000,2699)

#Function to find factorial of a number recursively
def factorial(n):       
    return 1 if (n==1 or n==0) else n * factorial(n - 1)

#Section to read each random integer and call factorial for the same
with open("Random_integer.txt") as f:
 for x in f: 
  n = int(x)  
  start = time.time()
  fact = factorial(int(n)) 
  t = '{:.20f}'.format(time.time()-start)
  id= id+1
  print('Request ID = '+str(id))
  print('N='+str(n)+' Factorial= '+ str(fact))
  print('Execution Time= '+t+' seconds')
  print('')

numfile.close()
