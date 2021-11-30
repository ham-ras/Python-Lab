nos=input("Enter a sequence of strings : ")
nos=list(map(int,nos.split(" ")))
for i in range (0,len(nos)) :
	if nos[i]>100 :
		nos[i]="Over 100"
print(nos)
