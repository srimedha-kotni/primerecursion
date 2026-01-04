def prime(n, i):
    if i == 1:
        return True
    if n % i == 0:
        return False
    return prime(n, i-1)
n = int(input("Enter a positive number: "))
if n > 1 and prime(n, n-1):
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")
