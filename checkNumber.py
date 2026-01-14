def is_armstrong(num):
    total = 0
    n = num

    power = len(str(num))

    while n > 0:
        digit = n % 10
        total += digit ** power

        n //= 10

    return total == num

def is_pelindrome(num):
    original = num 
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit

        num //= 10

    return reverse == original 

number = int(input("Enter a number: "))

if is_armstrong(number):
    print(number, " is an armsterong")

else:
    print(number,"is not an armstrong")

if is_pelindrome(number):
    print(number,"is a pelinddrome")

else:
    print(number,"is not a pelindrome")



