# Desafio Dev Python - 2022

Neste desafio foram desenvolvidos 3 programas para avaliação de strings visando a aplicação em NLPs. O primeiro visa identificar substrings dentro de strings, os segundo determina se os caracteres '[ { (' foram abertos e , caso positivo, se foram fechados. Por fim, o terceiro programa separa um texto em sentenças menores, as avalia quanto à presença de certas expressões (expressões.txt) e a posição destes, avaliando se a mesma se encontra entre os 3 primeiros tokens da sentença e compilando o resultado em um dicionário disposto em JSON.

Orientações gerais:

* Os arquivos estão nomeados como **desafio1**, **desafio2** ou **desafio3**, referindo-se para seu respectivo problema.
* Os módulos utilizados foram "JSON" e "Re (regex)".
------------------------------------------------

## Problema 1 - Identificação de substrings

Quando executar o script, o usuário será requisitado a inserir se quer ou não diferenciar letras maiúsculas e minúsculas digitando s ou n no terminal. Em sequência será requisitado os "strings" a serem avaliados.

A comparação entre "strings" é feita dentro de um loop for para ir variando a posição dentro do "string 1" e comparando com o "string 2".

------------------------------------------------

## Problema 2 - Validação de sequência de caracteres

Quando executar o script, o usuário será requisitado a inserir o conjunto de caracteres a serem avaliados como par. A lógica utilizado foi de manter uma lista de controle, de modo a adicionar um caractere de abertura quando o mesmo aparecer **antes** de um caractere de fechamento, excluindo o mesmo da lista caso seja feito um par. Ao fim do script, caso a lista esteja vazia, o usuário recebe a confirmação "True". Uma lista vazia também é considerada válida.

Aparecimento de um caractere de fechamento sozinho ou um par não fechado levam geram uma resposta "False".

------------------------------------------------

## Problema 3 - Verificação de expressões em sentenças

Quando executar o script, o usuário será requisitado para inserir o nome do arquivo JSON a ser analisado. O arquivo deve estar na mesma pasta que o script, tal como acompanhar a extensão no nome, como o exemplo dado "textos.json".

A ideia aplicada foi de utilizar loops para ir checando a estrutura do arquivo de entrada, e posteriormente para ir checando as respectivas entradas das sentenças obtidas e da lista de expressão, cruzando os dados obtidos.

No script utilizei o módulo "Regex", talvez fosse mais adequado usar o "nltk", porém, como tive pouco contato com ele, resolvi usar com um módulo mais familiar para mim. Um outro problema que tive, e não consegui resolver corretamente, foi no "dump" do JSON, onde mesmo desativando o "ensure_ascii" alguns caracteres especiais não ficam apresentados corretamente.

O arquivo **output_tharik.json** é um exemplo do resultado do script utilizando como entrada o **textos.json**.
------------------------------------------------
