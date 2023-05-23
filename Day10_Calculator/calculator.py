def add (n1, n2):
  return n1 + n2

def subtract (n1, n2):
  return n1 - n2

def mutiply (n1, n2):
  return n1 * n2

def divide (n1, n2):
  return n1 / n2

operations ={
  "+": add,
  "-": subtract,
  "*": mutiply,
  "/": divide,
}

def calculate ():
  calcOver = False
  num1 = float(input("What is the first number?"))
  while calcOver == False:
    for key in operations:
      print(key)
    symbol = input("What is the operation?")
    num2 = float(input("What is the second number?"))
    function = operations[symbol]
    answer = function(num1, num2)
    print(f"{num1} {symbol} {num2} = {answer}")
  
    isCalcOver = input(f"Type 'y' to continue calculating with {answer}, 'n' to exit")
    if isCalcOver == "y":
      num1 = answer
    else:
      calcOver = True

calculate()