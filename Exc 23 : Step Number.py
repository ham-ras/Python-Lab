num=int(input("Enter the number of steps of the pyramid"))
for i in range(1,num+1) :
	print("")
	for j in range(1,num+1) : 
		s=i*j
		print(s,end=" ")

