#n сразу же вводится через последний пробел
new_str = str(input())
new_list = new_str.split()
n = int(new_list.pop())
numbers = [int(x) for x in new_list[-1::-1]]
squared_numbers = []
for x in numbers:
  snumb = x ** n
  squared_numbers.append(snumb)
squared_numbers.reverse()
print(squared_numbers)
