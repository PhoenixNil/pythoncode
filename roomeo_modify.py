fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:#一行一行搜索
    for word in line.split():
        lst.append(word)    
lst.sort()
print(lst)

  
 
    
   
   
  
#                            使用一个嵌套循环就可以了，第一个循环从行搜索，第二个循环就是遍历每一行就行了！！！，
#                     感觉自己好蠢啊外国人就这么厉害吗？