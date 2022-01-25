def pattern(num):
	for i in range(1,num+1) :
		print("")
		for j in range(1,i+1) : 
			s=i*j
			print(s,end=" ")
num=int(input("Enter the number of steps of the pyramid"))
pattern(num)
