str1=input("Enter the the values of first list : ")
str2 = input("Enter the values of second list : ")
str1 = list(map(int,str1.split(" ")))
str2 = list(map(int,str2.split(" ")))
if len(str1)==len(str2) : 
	print("Both the lists are equal")
elif len(str1)>len(str2) : 
	print("List 1 is greater than List 2")
else :
	print("List 2 is greater than List 1")
sum1=sum(str1)
sum2=sum(str2)
if (sum1==sum2) : 
	print("Values of both the list sums to equal : ",sum1)
elif (sum1>sum2) :
	print("Sum of List 1 is greater than List 2")
else : 
	print("Sum of List 2 is greater than List 2")
commonvalue = []
#for i in str1 : 
	#for j in str2 : 
		#if i==j :
			#commonvalue.append(i)
for i in str1 :
	if i in str2 : 
		commonvalue.append(i)
print("\nCommon values in both lists are ",commonvalue)
