a, b = input().split()
a = int(a)
b = int(b)
gcd = lambda a, b: a if not b else gcd(b, a % b)
lcm = int(a * b / gcd(a, b))
answer = [gcd(a, b), lcm]
print(gcd(a, b))
print(lcm)
