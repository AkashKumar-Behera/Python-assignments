msgs="hello world python"
l=msgs.split() # l= ['hello', 'world', 'python']
k=sorted(l) # k= ['hello', 'python', 'world']
m="-".join(k) #m= 'hello-python-world'
print(m)