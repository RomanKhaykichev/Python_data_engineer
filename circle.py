animals = ['cat', 'dog', 'humster']

for i, animal in enumerate(animals, start=1):
    print(i, animal)


data = 0
while data < 100:
    data += 3
    if data % 19 == 0:
        continue
    data +=1
    if data % 40 == 0:
        break
else:
    data += 5
print(data)


arr = [5, 5, 2, 5, 5, 2, 2, 2]
for number in arr:
    input = ''
    for i in range(number):
        input += '*'
    print(input)