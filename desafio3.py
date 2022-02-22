#importar json e abrir documento.
import json
import re
arquivo_json = input("Digite o nome do arquivo JSON a ser analisado: \n")
#carregar arquivos, problema com utf-8.
with open(arquivo_json, encoding='utf-8') as f_texto:
    f_expressao = open('expressoes.txt', 'r', encoding='utf-8')
    textos = json.load(f_texto)
#criar lista de saída para o JSON.
    output_list = []

#loop para separar expressões e criar uma lista com todas.
    expressao_list = []
    for line in f_expressao:
        line_list = line.split()
        expressao_list.append(line_list)

#loop para ler cada dicionário da lista e separar sentenças.
    for d in textos:
        output_dic = {"id": d["id"], "sentenças": []}
        texto_str = d["texto"].lower()
        sentencas_lst = re.split(r'(?<=[.!?]) ', texto_str)
#Dicionário e lista para acompanhamento.
        sent_exp_dic = {}
        sent_exp_lst = []
#Loop para checar presença de expressões.
        for sentenca in sentencas_lst:
            tokens_sent = re.findall(r"[\w']+|[.,!?;]", sentenca)
            for exp in expressao_list:
                exp_str = ' '.join(exp)
#Checa se o string da expressão está presente na sentença e se é ums dos 3 primeiros tokens da sentença.
                if exp_str in sentenca and exp[0] in tokens_sent[:3]:
                    sent_exp_dic = {"sentença": sentenca, "expressão": exp_str}
                    break
#Caso não dê fit com as expressôes, adiciona como expressão "nulo".
                else:
                    sent_exp_dic = {"sentença": sentenca, "expressão": None}

#Formar lista de expressão de sentença.
            sent_exp_lst.append(sent_exp_dic)
            output_dic["sentenças"] = sent_exp_lst

#Formar lista de saída e produzir json.
        output_list.append(output_dic)
        out_file = open("output_tharik.json", "w")
        json.dump(output_list, out_file, indent=6, ensure_ascii=False)
        out_file.close()
