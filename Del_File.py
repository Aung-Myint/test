import os
os.remove('demo2.txt')
create_demo2=open('demo2.txt','x')
print(os.path.exists('demo2.txt'))
if os.path.exists('demo2.txt')==True:
    os.remove('demo2.txt')
    print('file deleted')
else :
    print('file not exits')