# Obter a string do usuário
string = input("Digite uma string: ")

# Converter a string em uma lista de caracteres
lista_chars = list(string)

# Inverter a lista de caracteres
tamanho = len(lista_chars)
for i in range(tamanho//2):
    temp = lista_chars[i]
    lista_chars[i] = lista_chars[tamanho-1-i]
    lista_chars[tamanho-1-i] = temp

# Converter a lista de caracteres de volta para uma string
string_invertida = ''.join(lista_chars)

# Imprimir a string invertida
print("A string invertida é:", string_invertida)
