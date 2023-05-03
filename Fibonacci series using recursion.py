def rec_fibo(n):
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return rec_fibo(n-2) + rec_fibo(n-1)


nterms = int(input("how many series: ")) 
for i in range(nterms):
    print(rec_fibo(i))