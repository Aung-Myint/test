x='hello world!'
print(x)
#multi line use three single quote or double quote
x='''How to assign Multiline string?\nHow to assign Multiline String?'''
print(x)
print(len(x))
#search first character
print(x[0])
#search last character
print(x[-1])
print('string' in x)#check word in quote are exist
print("strings" in x)#check word in quote are exist
#check word in quote are not exist
print('are' not in x)
print('string' not in x)
name= "Aung Myint"
age="27"
print('My name is '+ name +' and I am '+str(age)+' years old')
#assign by argument
print('My name is {name} and I am {age} years old'.format(name=name,age=age))
#f string
print(f'My name is {name} and I am {age} years old')