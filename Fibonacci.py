n = int(input("Enter a number: "))
n1 , n2 =0,1
sum= 0

if n<=0:
    print("Number should be greater than 0")

else:
    for i in range(0,n):
        print(sum, end=' ')
        n1 = n2
        n2 = sum
        sum = n1 + n2
        


