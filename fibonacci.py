import random
#Section to create and store 100 random integers
numfile = open("fibo.txt", "w")
for i in range(100):
    line = str(random.randint(1,100)) + '\n'
    numfile.write(line)
    #print(line)
numfile.close()

with open("fibo.txt") as f:
 for x in f: 
  n = int(x)
  print("Fib of ",n,"is = ")  
  fib(n)
  print("\n") 
  

#fib(10)
def fib(Number):  
   First_Value = 0
   Second_Value = 1
   for Num in range(0, Number):
            if(Num <= 1):
                       Next = Num
            else:
                       Next = First_Value + Second_Value
                       First_Value = Second_Value
                       Second_Value = Next
            print(Next,end=' ')
            print(" ")