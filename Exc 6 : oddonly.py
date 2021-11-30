a = input("Enter a sequence of nos : ")
a = list(map(int,a.split(" ")))
oddlist=[]
oddlist=[i for i in a if i%2!=0]
print("The list after removing even nos is : ",oddlist)
