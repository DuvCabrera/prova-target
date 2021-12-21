def fibonacci(n):
    pertence = "O número pertence à sequência"
    n_pertence = "o número informado não pertence à sequência"
    t_final= 1
    t_inicial = 0
    if n <= 3 and n >= 0 :
        print(pertence)
    else:
        contem = False
        contador = 0
        while contador < n:
            soma = t_inicial + t_final
            t_inicial = t_final
            t_final = soma
            contador += 1
            if soma == n:
                contem = True
                print(pertence)
                break
            elif soma > n:
                break
        if contem == False:
            print(n_pertence)
