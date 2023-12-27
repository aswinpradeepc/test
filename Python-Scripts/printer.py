import math  

n = int(input("Enter number of pages in pdf :"))
pps = int(input("Enter number of pages to be printed per sheet :"))

x=n//pps
math.ceil(x)

o,e=[],[]


for i in range(1,n,2*pps):
	for k in range(0,pps):
		if i+k <= n:
			o.append(i+k)
		if i+k+pps <= n:
			e.append(i+k+pps)
	"""	
for i in range(pps+1,n+1,2*pps):
	for k in range(0,pps):
		if i+k <= n:
			e.append(i+k)"""
		
print(o)
print(e)
