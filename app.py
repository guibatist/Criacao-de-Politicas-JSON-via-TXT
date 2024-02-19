# Lógica do arquivo txt
# - O nome do arquivo - no exemplo é "teste1" -, não pode conter a extenção "".json"
# - Não pode conter espaços entre o nome json pro "/", do "/" pros nomes dos campos, e o nome dos campos pro ";"
# teste1/id;status

# teste1 é o arquivo json
# / separa a tabela
# id e status são os campos a ser editado
# se tem mais de um, são separados por ;


import json
import os

def adicionar_politica(campo, politica):
    campo['policyTags'] = politica

def ler_e_adicionar_politica(arquivo_txt):
    with open(arquivo_txt + '.txt', 'r') as arquivo:
        for linha in arquivo:
            partes = linha.strip().split("/")
            nome_json = partes[0]
            campos_para_editar = partes[1].split(';')

            nome_json += '.json'

            if os.path.exists(nome_json):
                with open(nome_json, 'r') as json_file:
                    data = json.load(json_file)
                    politica = {
                        "names": [
                            "projects/projeto/locations/us-east1/taxonmies/1234/policyTags/1231423"
                        ]
                    }
                    for campo in data:
                        if campo['name'] in campos_para_editar:
                            adicionar_politica(campo, politica)
                        if campo['name'] == 'addresses':
                            for endereco in campo['fields']:
                                if endereco['name'] in campos_para_editar:
                                    adicionar_politica(endereco, politica)

                with open(nome_json, 'w') as json_file:
                    json.dump(data, json_file, indent=4)
            else:
                print(f"O arquivo {nome_json} não foi encontrado.")

# Localização do arquivo de texto
arquivo_txt = "arquivo_de_configuracao"

# Ler e adicionar as políticas
ler_e_adicionar_politica(arquivo_txt)
