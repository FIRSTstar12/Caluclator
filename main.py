equation = input()
spltEquation = equation.split(' ')
equation = []
symbols = []
vaild = True
for i in spltEquation:
  if i.strip('-').isdigit():
    equation.append(int(i))
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
    print('Invalid equation')
    vaild = False
    break
if not vaild:
  print('\n')
else:
  print(f"The answer is {equation}")