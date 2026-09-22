s="Hello World Hello"
list1=s.split()
dict1={}
for i in list1:
    if i in dict1:
        dict1[i]+=1
    else:
        dict1[i]=1
print(dict1)