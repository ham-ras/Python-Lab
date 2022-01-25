def factor(num):
    print("the factors of %d are : "%num)
    for i in range(1,num+1):
        if(num%i==0):
            print(i)
num=int(input("Enter a number : "))
factor(num)
