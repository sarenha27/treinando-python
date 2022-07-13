cont = 0
soma = 0
for h in range(6):
    n = float (input())
    if n>0:
        cont = cont + 1
        soma = soma + n 
media = soma / cont 
print(cont,"valores positivos")
print (f"{media:.1f}")