#create set
fruits={'apple','orange'};
print(fruits);
print(type(fruits));
#set are used with constructor
country=({'uk','us'});
print(country);
print (len(country));
print(type(country));
#access through loop
for fruit in fruits:
    print(fruit,type(fruit));
# add item using add()
country.add('mm');
print(country);
#merging two set using update()
another_fruits={'strawberry','cherry'};
fruits.update(another_fruits);
print(fruits);          
#remove item from set using remove()
fruits.remove('strawberry');
print(fruits);
#remove item from set using discard()
fruits.discard('strawberry');
print(fruits);
# fruits.remove('strawberry');
# print(fruits);
#clear all item from set
fruits.clear();
print(fruits);
#Delete set
del fruits;
print(fruits);