# Projeto API de Endereços 📜
## Descrição
Este projeto oferece uma API RESTful que permite aos usuários buscar informações sobre cidades, incluindo dados relacionados à sua região imediata, microrregião, mesorregião, e estado.

Por exemplo, ao buscar por "Patos", a API retorna informações sobre a cidade de Patos, na Paraíba, incluindo detalhes sobre a microrregião de Patos, mesorregião do Sertão Paraibano, e a região Nordeste do Brasil.

python manage.py runserver

## Como usar

Endpoint: Pesquisa de Cidades
URL: https://api-address.aplicacao-tech.com.br/search/

Método: GET

Parâmetros:

nome: Nome da cidade a ser pesquisada
Exemplo de chamada:

bash
Copy code
curl -X GET "https://api-address.aplicacao-tech.com.br/search/?nome=Patos"

## Resposta:

Retorna um JSON contendo as informações da cidade buscada, incluindo a microrregião, mesorregião, e estado.

Exemplo:

json
Copy code
{
  "data": {
    "id": 2510808,
    "nome": "Patos",
    ...
  }
}

## Deploy com Gunicorn e Supervisor

O projeto está configurado para ser executado com Gunicorn. Um exemplo de configuração do Supervisor para este projeto pode ser encontrado no arquivo supervisor.conf.

## Contribuições

Pull requests são bem-vindos. Para mudanças importantes, por favor abra uma issue primeiro para discutir o que você gostaria de mudar.
