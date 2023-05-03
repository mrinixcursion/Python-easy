num = int(input("Enter a number: "))
sum = 0
temp = num

n= len(num)

while temp > 0:
    digit = temp % 10
    sum += digit**n
    temp //=10

if sum == num:
    print("Yes it's an armstrong number")
else:
    print("No it's not an armstrong number")

