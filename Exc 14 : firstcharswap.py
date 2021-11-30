s1 = input("Enter first string : ")
s2 = input("ENter second string : ")
new_s1 = s2[0] + s1[1:]
new_s2 = s1[0] + s2[1:]
s3 = new_s1 + " " + new_s2
print("Combined strings with characters swapped : ",s3)

