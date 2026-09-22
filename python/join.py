s=""
l=[]
for i in range(65, 91):
    # s += chr(i)
    l.append(chr(i))
s = " ".join(l)
print(f"{s} all capital letters of the English alphabet")

num=int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} * {i} = {num*i}")
    print(num,"*",i,"=",num*i)
