fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:#一行一行搜索
    words=line.rstrip()
    word=words.split()
    if word is not lst :
        for i in word :
            lst.append(i)  
lst2=list(set(lst))
lst2.sort()
print(lst2)




#                                找罪受！