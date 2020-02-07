# Función para calcular la suma de
# los N primeros números

def sumn(n):
    res=0
    for i in range(1,n+1):
        res +=i
    return res

# El programa principal empieza aquí

print("La suma de los primeros 20 números enteoros es: ", sumn(20))
print("La suma de los primeros 100 números enteoros es: ", sumn(100))
