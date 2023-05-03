num = int(input("ENter a number: "))
reverse , temp = 0, num

while temp != 0:
    reverse = reverse* 10 + temp%10
    temp //= 10

if reverse == num:
    print("number is palindrome")
else:
    print("Number is not palindrome")