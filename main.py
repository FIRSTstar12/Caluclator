import math
#+, -, *, /
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
#^,sqrt,abs
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
#spimplifing fractions
def fractionSimplification():
  numerator = int(input("Enter the numerator: "))
  denominator = int(input("Enter the denominator: "))
  gcd = math.gcd(numerator, denominator)
  numerator = numerator / gcd
  denominator = denominator / gcd
  return numerator / denominator
#Idenifing systems of equations
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
#Unit rates
def unitRates():
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
#unit Conversion m, km, cm, mm, mi
def unitConversion():
  print('m = meter\n km = kilometer\n cm = centimeter\n mm = millimeter\n mi = mile')
  unit = input('What unit are you converting from? ')
  unit2 = input('What unit are you converting to? ')
  num = float(input('How much of the unit are you converting? '))
#cm and m
  if (unit == 'cm') and (unit2 == 'm'):
    cmToM = num / 100
    print(cmToM)
  elif (unit == 'm') and (unit2 == 'cm'):
    mToCm = num * 100
    print(mToCm)
#cm and km
  elif (unit == 'cm') and (unit2 =='km'):
    cmToKm = num / 100000
    print(cmToKm)
  elif (unit == 'km') and (unit2 == 'cm'):
    kmToCm = num * 100000
    print(kmToCm)
#cm and mi
  elif (unit == 'cm') and (unit2 == 'mi'):
    cmToMi = num / 160934
    print(cmToMi)
  elif (unit == 'mi') and (unit2 == 'cm'):
    miToCm = num * 160934
    print(miToCm)
#cm and mm
  elif (unit == 'mm') and (unit2 == 'cm'):
    mmToCm = num / 10
    print(mmToCm)
  elif (unit == 'cm') and (unit2 == 'mm'):
    cmToMm = num * 10
    print(cmToMm)
#km and mi
  elif(unit == 'km') and (unit2 == 'mi'):
    kmToMi = num / 1.609
    print(kmToMi)
  elif(unit == 'mi') and (unit2 == 'km'):
    miToKm = num * 1.609
    print(miToKm)
#km and m
  elif(unit == 'km') and (unit2 == 'm'):
    kmToM = num * 1000
    print(kmToM)
  elif(unit == 'm') and (unit2 == 'km'):
    mToKm = num / 1000
    print(mToKm)
#km and mm
  elif(unit == 'km') and (unit2 == 'mm'):
    kmToMm = num * 1000000
    print(kmToMm)
  elif(unit == 'mm') and (unit2 == 'km'):
    mmToKm = num / 1000000
    print(mmToKm)
#mm and m
  elif(unit == 'mm') and (unit2 == 'm'):
    mmToM = num / 1000
    print(mmToM)
  elif(unit == 'm') and (unit2 == 'mm'):
    mToMm = num * 1000
    print(mToMm)
#mm and mi
  elif(unit == 'mm') and (unit2 == 'mi'):
    mmToMi = num / 160934
    print(mmToMi)
  elif(unit == 'mi') and (unit2 == 'mm'):
    miToMm = num * 160934
    print(miToMm)
#m and mi
  elif(unit == 'm') and (unit2 == 'mi'):
    mToMi = num / 1609.34
    print(mToMi)
  elif (unit == 'mi') and (unit == 'm'): 
    miToM = num * 1609.34
    print(miToM)
#area of a shape
def areaOfShape():
  shape = input('What shape are you finding the area of? ')
  if shape == 'square':
    length = float(input('What is the length of the square? '))
    area = length ** 2
    return area
  elif shape == 'rectangle':
    length = float(input('What is the length of the rectangle? '))
    width = float(input('What is the width of the rectangle? '))
    area = length * width
    return area
  elif shape == 'triangle':
    base = float(input('What is the base of the triangle? '))
    height = float(input('What is the height of the triangle? '))
    area = base * height / 2
    return area
  elif shape == 'circle':
    radius = float(input('What is the radius of the circle? '))
    area = math.pi * radius ** 2
    return area
  elif shape == 'trapezoid':
    base1 = float(input('What is the length of the first base? '))
    base2 = float(input('What is the length of the second base? '))
    height = float(input('What is the height of the trapezoid? '))
    area = (base1 + base2) / 2 * height
    return area
  elif shape == 'parallelogram':
    base = float(input('What is the base of the parallelogram? '))
    height = float(input('What is the height of the parallelogram? '))
    area = base * height
    return area
  elif shape == 'rhombus':
    diagonal1 = float(input('What is the length of the first diagonal? '))
    diagonal2 = float(input('What is the length of the second diagonal? '))
    area = diagonal1 * diagonal2 / 2
    return area
  else:
    return 'Invalid shape'
#volume of a shape
def volumeOfShape():
  shape = input('What shape are you finding the volume of? ')
  if shape == 'cube':
    length = float(input('What is the length of the cube? '))
    volume = length ** 3
    return volume
  elif shape == 'rectangular prism':
    length = float(input('What is the length of the rectangular prism? '))
    width = float(input('What is the width of the rectangular prism? '))
    height = float(input('What is the height of the rectangular prism? '))
    volume = length * width * height
    return volume
  elif shape == 'cylinder':
    radius = float(input('What is the radius of the cylinder? '))
    height = float(input('What is the height of the cylinder? '))
    volume = math.pi * radius ** 2 * height
    return volume
  elif shape == 'cone':
    radius = float(input('What is the radius of the cone? '))
    height = float(input('What is the height of the cone? '))
    volume = math.pi * radius ** 2 * height / 3
    return volume
  elif shape == 'sphere':
    radius = float(input('What is the radius of the sphere? '))
    volume = 4/3 * math.pi * radius ** 3
    return volume
  elif shape == 'pyramid':
    base = float(input('What is the base of the pyramid? '))
    height = float(input('What is the height of the pyramid? '))
    volume = base ** 2 * height / 3
    return volume
  elif shape == 'prism':
    base = float(input('What is the base of the prism? '))
    height = float(input('What is the height of the prism? '))
    volume = base * height
    return volume
  else:
    return 'Invalid shape'
#probibility
def probibility():
  event = int(input('How many events are there? '))
  sample = int(input('How many samples are there? '))
  prob = event / sample
  return prob
#percentages
def percents():
  num = float(input('What is the number? '))
  percent = float(input('What is the percent? '))
  percent = percent / 100
  answer = num * percent
  return answer
#percent increase
def percentIncrease():
  num = float(input('What is the number? '))
  percent = float(input('What is the percent? '))
  percent = percent / 100
  answer = num * percent + num
  return answer
#percent decrease
def percentDecrease():
  num = float(input('What is the number? '))
  percent = float(input('What is the percent? '))
  percent = percent / 100
  answer = num - num * percent
  return answer

guide = print('1 = Basic Math(+,-,*,\) \n2 = Fraction Simplification\n3 = Systeme of Equations\n4 = Unit Rate\n5 = Advanced Math(^,sqrt,abs)\n6 = Unit Conversion\n7 = Area of a shape\n8 = Volume of a shape\n9 = probibilty\n10 = percents\n11 percent increase\n12 percent decrease \n13 = Quit')
quit = False
while not quit:
  typeOfMath = int(input('Enter the type of math you want to do: '))
  if typeOfMath == 1:
    print(f" The answer is {basicMath()}")
    quit = True
  elif typeOfMath == 2:
    print(f" Your problem has {systemeOfEquations()}")
    quit = True
  elif typeOfMath == 3:
    print(f" The is the simplist form of your fraction: {fractionSimplification()}")
    quit = True
  elif typeOfMath == 4:
    print(f"Your unit rate is: {unitRates()}")
    quit = True
  elif typeOfMath == 5:
    print(f"The answer is {advancedMath()}")
    quit = True
  elif typeOfMath == 6:
    unitConversion()
    quit = True
  elif typeOfMath == 7:
    print('square\n rectange\n triangle\n circle\n trapezoid\n parallelogram\n rhombus\n')
    print(areaOfShape)
    quit = True
  elif typeOfMath == 8:
    print('cube\n rectangular prism\n cylinder\n cone\n sphere\n pyramid\n prism')
    print(volumeOfShape)
  elif typeOfMath == 9:
    print(f"The probibility is {probibility()}")
  elif typeOfMath == 10:
    print(f"The percent is {percents()}")
  elif typeOfMath == 11:
    print(f"The percent increase is {percentIncrease()}")
  elif typeOfMath == 12:
    print(f"The percent decrease is {percentDecrease()}")
  elif typeOfMath == 13:
    quit = True
  else:
    print('Invalid input')
    quit = False
