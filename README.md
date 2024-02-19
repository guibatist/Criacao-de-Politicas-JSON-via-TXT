# Criacão de Politicas de Tabelas JSON via TXT

Projeto de Aplicação de Políticas em Arquivos JSON

Este script Python tem o objetivo de aplicar políticas específicas em campos de arquivos JSON de acordo com as configurações fornecidas em um arquivo de texto de configuração.

Arquivo de Configuração:
- O arquivo de configuração contém as informações sobre quais arquivos JSON devem ser editados e quais campos específicos desses arquivos devem receber a política.
- Cada linha do arquivo de configuração segue o formato:
  nome_arquivo_json/campo1;campo2
  Onde:
  - 'nome_arquivo_json' é o nome do arquivo JSON (sem a extensão '.json').
  - 'campo1;campo2' são os campos a serem editados, separados por ';'.
- Exemplo:
  teste1/id;status

Instruções de Uso:
1. Coloque os arquivos JSON a serem editados e o arquivo de configuração na mesma pasta que este script Python.
2. Execute o script e ele lerá automaticamente o arquivo de configuração e aplicará as políticas conforme especificado.

Por favor, certifique-se de fornecer o arquivo de configuração com as informações corretas para garantir que os arquivos JSON sejam editados corretamente.
