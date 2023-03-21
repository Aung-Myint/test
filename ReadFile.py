dm_file=open('demo.txt','rt')
print(dm_file.read(5))
print(dm_file.readline())
for x in dm_file:
    print(x)
dm_file.close()