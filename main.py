# break

my_list = [1,2,3]

for item in my_list:
  print(item)
  break

i = 0 
while i < 50:
  print(my_list[i])
  i += 1
  break


# Continue 

list_2 = [4,5,6]

# continue takes thee code back to the top of the for or while loop
for item in list_2:
  print(item)
  continue



i = 0 
while i < len(list_2):
  i += 1
  continue
  print(list_2[i])

list_3 = [7,8,9]

# this returns nothing because continue returns to the top of the for loop
for item in list_3:
  continue
  print(item)

# this returns nothing because continue returns to the top of the while loop
i = 0 
while i < len(list_3):
  i += 1
  continue
  print(list_3[i])

# pass

# pass is usefull as a placeholder when you have a loop and are not sure waht do write inside it yet 

list_4 = ['a','b','c']
for i in list_4:
  # you need to fill this in or else you will get an error so you can use pass as a placeholder
  pass

i = 0 
while i < len(list_4):
  print(list_4[i])
  i += 1
  pass