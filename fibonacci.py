import random
#Section to create and store 100 random integers
numfile = open("fibo.txt", "w")
for i in range(100):
    line = str(random.randint(1,100)) + '\n'
    numfile.write(line)
    #print(line)
numfile.close()

#Section to calculate the fibonacci series
def fib(numb):  
   val1 = 0
   val2 = 1
   for Num in range(0, numb):
            if(Num <= 1):
                       Next = Num
            else:
                       Next = val1 + val2
                       val1 = val2
                       val2 = Next
            print(Next,end=' ')
            

#logic to open random integer file and call fibonacci func for the same
with open("fibo.txt") as f:
 for x in f: 
  n = int(x)
  print("Fib of ",n,"is = ")  
  fib(n)
  print("\n") 
  
