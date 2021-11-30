n=int(input("Enter a no to check armstrong : ")
copy=n
while n!=0
	rem = n%10
	sum = (sum*10) + (rem*rem*rem)
	n=n//10
if sum==copy :
	print("The no is armstrong")
else : 
	print("The no is not armstrong")

