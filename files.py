du=input('Enter files name :')
f=open(du)
for line in f.readlines():
    K=line.strip()
    print(K.upper())