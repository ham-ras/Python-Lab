def fibon(limit):
	a=0
	b=1
	print(a,end=" ")
	for i in range(2,limit+1) : 
		c=a+b
		a=b
		b=c
		print(c,end=" ")
		i=i+1
limit=int(input("Enter the limit to find the fibonnaci : "))
fibon(limit)
