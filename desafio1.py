#Definir os input (String e subtring ou string1 e string2) e definir variável do contador.
distincao = input("Diferenciar caixa alta e caixa baixa? Digite s ou n: \n")
string1 = input("Digite S1: \n")
string2 = input("Digite S2: \n")
count = 0

#condicional para diferenciar caixa alta e baixa.
if distincao == "n":
    string1 = string1.lower()
    string2 = string2.lower()

#Fazer o recorte do tamanho do string2 e checar se é igual o string2.
#A range é melhor com nº de letras ou nºletras de s1 menos s2? Não achei problemas em nenhum das duas.

for i in range(len(string1)+1):
    if(string1[i:i+len(string2)] == string2):
        count += 1
print(count)

#Funcionou.
