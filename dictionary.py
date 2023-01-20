car={
    'brand':'bmw',
    'price':'$3000',
    'model':2020,
    'year':'2022'
}
print(car)
print(type(car))
#use constructor
fruit=dict(name="apple",price='$3')
print(fruit)
print(type(fruit))
#how many items in dictionary using len()function:
print(len(car))
#get item with key
print(fruit['name'])
print(fruit.get('price'))
print(car['brand'])
print(car.get('price'))
#add key/value in dict
fruit['name_2']='orange'
fruit['price_2']='$3'
print(fruit)
#get key
print(fruit.keys())
#get value
print(fruit.values())

#copy dict
another_car=car.copy()
print(another_car)
#removes the item with the specified key name using del keyword
del another_car['brand']
print(another_car)
#clear dict
another_car.clear()
print(another_car)
print(type(another_car))
#delete the dict
del another_car
print(another_car)
