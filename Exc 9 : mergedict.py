def newdict() : 
        a={}
        lim = int(input("Enter the no of values in dictionary : "))
        for i in range (0,lim) :
                key = input("Enter the key : ")
                value = input("Enter the value of key  : ")
                a[key]=value
        return a
dict1=newdict()
dict2=newdict()
print("Dictionary 1 : ",dict1)
print("Dictionary 2 : ",dict2)
dict1.update(dict2)
print("the dictionary after merging is ",dict1)
