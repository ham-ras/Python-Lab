n = int(input("Enter a number to reverse : "))
copy=n
rev=0
while n!=0 :
	dig = n%10
	rev = dig + rev*10
	n=n//10
print("Before reverse : ",copy)
print("After reverse : ",rev)

