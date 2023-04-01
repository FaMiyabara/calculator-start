from art import logo
print(logo)

def add(x,y):
  return x+y
def subtract (x,y):
  return (x-y)
def multiply (x,y):
  return x*y
def divide(x,y):
  return x/y

operations ={
  '+':add,
  '-':subtract,
  '*':multiply,
  '/':divide,
} 
def calculator():
  num1 = float(input("What's the first number? "))
  
  for operator in operations:
    print (operator)
  
  should_continue = True
  while should_continue:
    operation_symbol = input("Choose an operation : ")
    num2 = float(input("What's the next number? "))
    calculation_function = operations [operation_symbol]
    answer = calculation_function(num1,num2)
    print (f"{num1} {operation_symbol} {num2} = {answer}")
    if input(f'Type "y" to continue calculating with { answer} or "n" to start a new calculation ') == 'y':
      num1 = answer
    else:
      should_continue = False
      if input("Do you want to do another calculation? Tipe 'y' or 'n '") == 'y':
        calculator()
      else:
        break

calculator()