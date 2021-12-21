def inverte_str(string):
    tamanho_str = len(string)
    palavra_invertida = ""
    for letra in range(tamanho_str-1, -1, -1):
        palavra_invertida += string[letra]
    print(palavra_invertida)

#ou podemos fazer assim no python

def inverte_str2(string):
    print(string[::-1])