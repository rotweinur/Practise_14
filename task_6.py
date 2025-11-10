x = int(input())

divisors = set()

if x != 0:
    divisors.add(1)
    divisors.add(x)

n = abs(x)
for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        divisors.add(i)
        divisors.add(n // i)

result = sorted(divisors)
print(result)
    