#Criar listas para os pares, ambos indexados na mesma ordem. Seria melhor usar tupla?

abertura = ["(", "[", "{"]
fechamento = [")", "]", "}"]

#Função para checar se os pares estão presentes usando pares de indexadores.


def check(sequencia):
    conjunto = []
#Avaliar se a sequencia é vazia.
    if sequencia == [""]:
        return True
    else:
        #Checar primeiro se é abertura, se sim, checar se tem fechamento. Usei da ideia de manter um rastreio com a lista conjunto e, quando tiver uma abertura seguida de fechamento em algum momento, ir removendo com pop da lista.

        for i in sequencia:
            if i in abertura:
                conjunto.append(i)
            elif i in fechamento:
                pos_fech = fechamento.index(i)
                if ((len(conjunto) > 0) and (abertura[pos_fech] == conjunto[len(conjunto) - 1])):
                    conjunto.pop()
#Se for fechamento antes de abertura, retorna falso.
                else:
                    return False
#Se conjunto está vazio, todas as entradas são pares.
        if len(conjunto) == 0:
            return True
        else:
            return False


sequencia = input("Insira a sequência a ser avaliada:\n")
print(check(sequencia))
