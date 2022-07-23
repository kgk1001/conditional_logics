user = {'name': 'Gihan', 'age': 28, 'can_swim': True}
for item in user.items():
    print('item :', item)
for key, value in user.items():
    print(f"{key} : {value}")
for item in user.values():
    print('Values :', item)
for item in user.keys():
    print('Keys :', item)

print('1 to 10')
for _ in range(0, 10):
    print(_)

print('1 to 10 with 2 stepper')
for _ in range(0, 10, 2):
    print(_)

print('10 to 1')
for _ in range(10, 0, -1):
    print(_)

for _ in range(2):
    print(list(range(10)))

for index,char  in enumerate(list(range(100))):
  if char == 50:
    print(f'Index of 50 is {index}') 

x = 0
while x < 20:
  print (f'Number is {x}')
  x += 1
else:
  print('Count done ')

while True:
  input('say something : ')
  break
