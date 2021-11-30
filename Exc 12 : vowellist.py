a=input("Enter the sentence to select vowels : ")
a=list(a.strip())
print(a)
b=[i for i in a if i in "AEIOUaeiou"]
print(b)
