num1 = float(input())
num2 = float(input())
symbol = input()
if symbol == "+":
  add = num1 + num2
elif symbol == "-":
  add = num1 - num2
elif symbol == "*":
  add = num1 * num2
elif symbol == "/":
  add = num1 / num2
else:
  print("Invalid Input")
print(add)