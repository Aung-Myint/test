def sayHi():
    print('hi')
sayHi()
def greeting(msg):
    print(msg)
greeting('hello Everyone')
def adding(num1=0,num2=0):
    print(num1+num2)
adding(4)
def getNames(*name):
    print(name[0], name[1])
getNames('John', 'Leo')
def i_am(name,age):
    print(f'My name is {name} and I am {age} year old.')
i_am(20,'Kyaw Htet')
i_am(age=20,name='kyaw Htet')
def no_content():
    pass