n=int(input("enter the number"))
for i in range(1,n+1) :
	print("") 
	for j in range(1,i+1) : 
		print("*",end="")
for i in range(n-1,0,-1):
	print("")
	for j in range(i+1,1,-1):
		print("*",end="")



