import turtle 

def seq3np1(n):
  count = 0
  while(n != 1):
      count= count +1
      if(n % 2) == 0:        
        n = n // 2
      else:                
        n = n * 3 + 1
      #print(count)
  return count
  
def graph(upper_bound): 
  T1= turtle.Turtle()
  T2 = turtle.Turtle()
  wn=turtle.Screen()
  wn.setworldcoordinates(0,0,10,10)
  max_so_far= 0
  T2.goto(0,10)
  
  for x in range(1, upper_bound+1): 
    result= seq3np1(x)
    if result> max_so_far: 
      max_so_far = result
    T2.goto(0,max_so_far)
    string= "maximim so far:", x, result 
    T2.clear()
    T2.write(string)
    wn.setworldcoordinates(0,0, x+10, max_so_far+10)
    T1.goto(x, result)
  wn.exitonclick()    
  
def main():
  upper_bound = int(input("upper bound:"))
  if(upper_bound < 0):
    return
  for start in range(1, upper_bound+1):
    seq3np1(upper_bound)
    print("Current loop value: ", start, "Number of iterations: ", seq3np1(start))
  graph(upper_bound)
  seq3np1(3)
main()
