name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
address=dict()
email=list()
for line in handle :
    if not line.startswith("From ") : continue
    words=line.split()
    email.append(words[1])
for word in email:
    address[word]=address.get(word,0)+1
bigcount=0
bigword=None
for word,count in address.items():#word,count 对应两个变量一个是key，一个是value看清楚是逗号还是点，打印的是一个有键值的字典
    if bigcount<count:#如果现在的值显示的比以前小，就换位置
        bigword=word
        bigcount=count
print(bigword,bigcount)
