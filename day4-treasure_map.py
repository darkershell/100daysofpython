frutas = ['maçã', 'banana', 'cereja', 'damasco', 'banana']
indice_banana = frutas.index('banana')
print(indice_banana)

frutas = ['maçã', 'banana', 'cereja', 'damasco', 'banana']
indice_banana = frutas.index('banana', 2)  
print(indice_banana) 

frutas = ['maçã', 'banana', 'cereja', 'damasco']

try:
    indice_laranja = frutas.index('laranja')
except ValueError:
    indice_laranja = -1

print(indice_laranja)  # Saída: -1 (indicando que 'laranja' não está na lista)

