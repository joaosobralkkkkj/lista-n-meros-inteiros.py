# Criando uma lista para armazenar os números
numeros = []

# Solicita ao usuário que insira 5 números inteiros
for i in range(5):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numero)

# Calculando o maior, o menor e a soma dos números
maior = max(numeros)
menor = min(numeros)
soma = sum(numeros)

# Imprimindo os resultados
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
print(f"A soma dos números é: {soma}")