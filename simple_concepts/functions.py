#finding even or odd number
def even_odd(x):
  if x%2==0:
    return True
  return False
x = int(input("Please enter a number: "))
y = even_odd(x)
if y:
  print("This is an even number.")
else:
  print("This is an odd number.")

#calculating rectange area
def rectangle(x,y):
  return(x*y)
x = int(input("Please enter a number: "))
y = int(input("Please enter a second number: "))
print(rectangle(x,y))
  
