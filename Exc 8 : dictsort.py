a={}
lim = int(input("Enter the no of values in dictionary : "))
for i in range (0,lim) :
        key = input("Enter the key : ")
        value = input("Enter the value of key  : ")
        a[key]=value
print(a)
print("The sorted dictionary in ascending is : ",sorted(a.items()))
print("The sorted dictionary in descending is : ",sorted(a.items(),reverse=True))

