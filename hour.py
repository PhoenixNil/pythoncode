name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
distribution=dict()
hours=list()
temp=list()
for line in handle :
    if not line.startswith('From ') : continue 
    words=line.split()
    time=words[5]
    hour=time.split(':')
    hours.append(hour[0])
for number in hours :
    distribution[number]=distribution.get(number,0)+1
for k,v in sorted(distribution.items())                :
    print(k,v)