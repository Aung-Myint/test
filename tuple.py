#creat tuple
laptop = ('apple','dell','msi');
print(laptop , type(laptop));
# create tuple using constructor
juice=tuple(('apple','orange'));
print(juice,type(juice));
#to know how many item in tuple with len()
print(len(laptop));
print(len(juice));
#if you want to create a tuple with one item, you need to add, in the end.
#Otherwise python will not recognize as a tuple
fruits=('apple',)
print(fruits, type(fruits));
# Get value
print(fruits[0],laptop[0]); 
#Can't change value
#fruits[0]='orange';
#print(fruits);
#Delete tuple
del fruits;
print(fruits);

