laptop_brands=['apple','dell','razor']
for brand in laptop_brands:
    print(brand)
for letter in 'apple':
    print(letter)
numbers = list(range(1,11))
print(numbers)
for number in numbers:
    if number > 5 : break
    print(number)
for number in numbers:
    if number%2 == 0 : continue
    print(number)
for number in numbers:
    print(number)
else: print('finish')
x=['a','b','c','d']
y=['e','f','g','h']
for i in x :
    for t in y:
        print(i,t)
electric_car ="Telsa"
top_electric_car = {'Hyundai': 1, 'Telsa': 2,'Porsche':3}
for tp_car in top_electric_car :
    if tp_car == electric_car:
        print(f'{electric_car} is contain in top electric car brand')
        break
else :
    print(f'{electric_car} is not contain in list!')
    