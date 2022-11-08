#finds the largets common divisor of two numbers

def euklid(n1,n2):
    if n1==n2: return n1
    return euklid(min(n1,n2),abs(n1-n2))

print(euklid(66,64))
