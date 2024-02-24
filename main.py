import math
def basicMath():
  equation = input('Enter the equation: ')
  spltEquation = equation.split(' ')
  equation = []
  symbols = []
  vaild = True
  for i in spltEquation:
    if i.strip('-').isdigit():
      equation.append(float(i))
    else:
      symbols.append(i)
  for i in symbols:
    if i == '+':
      equation.append(equation.pop(0) + equation.pop(0))
    elif i == '-':
      equation.append(equation.pop(0) - equation.pop(0))
    elif i == '*':
      equation.append(equation.pop(0) * equation.pop(0))
    elif i == '/':
      equation.append(equation.pop(0) / equation.pop(0))
    else:
      vaild = False
      return 'Invalid equation'
  if not vaild:
    return '\n'
  else:
    return equation[0]
def advancedMath():
  equation = input('Enter the equation: ')
  spltEquation = equation.split(' ')
  equation = []
  symbols = []
  vaild = True
  for i in spltEquation:
    if i.strip('-').isdigit():
      equation.append(float(i))
    else:
      symbols.append(i)
  for i in symbols:
    if i == '^':
      equation.append(equation.pop(0) ** equation.pop(0))
    elif i == 'sqrt':
      equation.append(math.sqrt(equation.pop(0)))
    elif i == 'abs':
      equation.append(abs(equation.pop(0)))
    else:
      vaild = False
      return 'Invalid equation'
  if not vaild:
    return '\n'
  else:
    return equation[0]
  equation = input('Enter the equation: ')
def fractionSimplification():
  numerator = int(input("Enter the numerator: "))
  denominator = int(input("Enter the denominator: "))
  gcd = math.gcd(numerator, denominator)
  numerator = numerator / gcd
  denominator = denominator / gcd
  return numerator / denominator
def systemeOfEquations():
  goe = input('Do you have a graph(g) or an equation(e)? ')
  if goe == 'g':
    lines = int(input('How many lines are there? '))
    if lines == 2:
      connect = input('Are the lines connected(y/n)? ')
      if connect == 'y':
          return "One soultion"
      else:
        return "No soultions"
    else:
      return "Infinite soultions"
  else:
    y1 = float(input('What is the slope of the first line? '))
    y2 = float(input('What is the slope of the second line? '))
    b1 = float(input('What is the y-intercept of the first line? '))
    b2 = float(input('What is the y-intercept of the second line? '))
    if y1 != y2:
      return "One soultion"
    elif (y1 == y2) and (b1 != b2):
      return "No soultions"
    elif (y1 == y2) and (b1 == b2):
      return "Infinite soultions"
def untRate():
  numerator = int(input("Enter the numerator: "))
  denominator = int(input("Enter the denominator: "))
  gcd = math.gcd(numerator, denominator)
  numerator = numerator / gcd
  denominator = denominator / gcd
  simp = print(f"{numerator}/{denominator}")
  if denominator == 1:
    return simp
  else:
    return f"{numerator}/{denominator}"

guide = print('1 = Basic Math(+,-,*,\) \n2 = Fraction Simplification\n3 = Systeme of Equations\n4 = Unit Rate\n5 = Advanced Math(^,sqrt,abs)')

typeOfMath = int(input('Enter the type of math you want to do: '))
if typeOfMath == 1:
  print(f" The answer is {basicMath()}")
elif typeOfMath == 2:
  print(f" Your problem has {systemeOfEquations()}")
elif typeOfMath == 3:
  print(f" The is the simplist form of your fraction: {fractionSimplification()}")
elif typeOfMath == 4:
  print(f"Your unit rate is: {untRate()}")
elif typeOfMath == 5:
  print(f" The answer is {advancedMath()}")
  
else:
  print('Invalid input')
