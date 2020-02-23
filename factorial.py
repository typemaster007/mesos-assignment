import random
#Section to create and store 100 random integers
numfile = open("Random_integer.txt", "w")
for i in range(100):
    line = str(random.randint(1,100)) + '\n'
    numfile.write(line)
    #print(line)
numfile.close()

def factorial(n):       
    return 1 if (n==1 or n==0) else n * factorial(n - 1)

#Section to read each random integer and find factorial for the same
with open("Random_integer.txt") as f:
 for x in f: 
  n = int(x)  
  fact = factorial(int(n))
  print("Factorial of ",n,"is =",fact)

numfile.close()