# Fatorial: N! = (N-1) x (N-2) x (...) x 1

def fat(n):
    acum = 1
    for x in range(1, n + 1):
        acum = acum * x
    return acum

def fatRec(n):
    if n == 0:
        return 1
    else:
        return n * fatRec(n-1)

print("Não recursivo")
print(fat(10))
print(fat(5))
print(fat(1))
print(fat(0))

print("Recursivo")
print(fatRec(10))
print(fatRec(5))
print(fatRec(1))
print(fatRec(0))