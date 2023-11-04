new_str = str(input())
index_otkr = 1 + new_str.find('(')
index_zakr = new_str.find(')')
index_otkr2 = 1 + new_str.rfind('(')
index_zakr2 = new_str.rfind(')')
vskob = new_str[index_otkr:index_zakr]
vskob2 = new_str[index_otkr2:index_zakr2]
print(vskob)
print(vskob2)
