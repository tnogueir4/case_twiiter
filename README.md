# Case_twiiter
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
<br/><br/>

Projeto para coleta dos tweets mais recentes com base em #tags predefinidas.

API desenvolvida com python e flask (micro-framework) para expor métricas como top 5 de usuários com mais seguidores, quantidade de posts por datetime e quantidade de posts de cada #tag por localização do usuário.

Default #tags:
#openbanking, #remediation, #devops, #sre, #microservices, #observability, #oauth, #metrics, #logmonitoring, #opentracing
<br/>


Tabela de conteúdos
=================
<!--ts-->
 - [APIs](#apis)
    - [Métodos](#metodos)
    - [Respostas](#resp)
    - [Recursos](#recursos)
 - [Arquitetura](#arquitetura)
 - [Como usar](#comousar)
 - [Logs](#logs)
 - [Dashboards](#dashboards)
<!--te-->

## <a name="apis">APIs</a>
O projeto Case_twiiter disponibiliza uma API REST que permite o consumo de alguns dados extraidos das API´s do Twitter.

Recursos disponíveis via API:
 * Top 5 usuários com mais seguidores.
 * Total de posts, agrupadas por hora do dia independente da #tag.
 * Total de posts para cada uma das #tags por localização do usuário que postou.

 ## <a name="metodos">Métodos</a>
Requisições para a API devem seguir os padrões:
| Método | Descrição |
|---|---|
| `GET` | Retorna informações de um ou mais registros. |
| `POST` | Utilizado para criar um novo registro. |
| `DELETE` | Remove um ou mais registros. |

## <a name="resp">Respostas</a>

| Código | Descrição |
|---|---|
| `200` | Requisição executada com sucesso (success).|
| `400` | Erros de validação ou os campos informados não existem no sistema.|
| `401` | Dados de acesso inválidos.|
| `404` | Registro pesquisado não encontrado (Not found).|
| `405` | Método não implementado.|
| `410` | Registro pesquisado foi apagado do sistema e não esta mais disponível.|
| `422` | Dados informados estão fora do escopo definido para o campo.|
| `429` | Número máximo de requisições atingido. (*aguarde alguns segundos e tente novamente*)|

## <a name="recursos">Recursos</a>

## Dados de usuários [/USERS/FOLLOWERS/TOP5] <br/>
<b>Listar (list) [GET /USERS/FOLLOWERS/TOP5]</b> <br/>
Cria uma lista com os 5 usuários com mais seguidores.

```
+ Request (application/json)

    + Body


+ Response 200 (application/json)

    + Body
            {
                "username": "test_user04",
                "followers": 999999
            },
            {
                "username": "test_user01",
                "followers": 999999
            },
            {
                "username": "test_user03",
                "followers": 989999
            },
            {
                "username": "Growth Hackers 🚀",
                "followers": 175317
            },
            {
                "username": "Growth Hackers 🚀",
                "followers": 175317
            }
```

<br/>

## Dados de usuários [/USERS/FOLLOWERS/TOP5/ADD] <br/>
<b>Novo (create) [POST /USERS/FOLLOWERS/TOP5/ADD]</b><br/>
Inclui um novo registro de usuário / seguidores.

```
+ Request (application/json)

    + Body
            {
                "username": "test_user04",
                "followers": 999999
            }


+ Response 200 (application/json)

    + Body
            {
            "mensagem": "Inserted record",
            "followers": {
                "username": "test_user04",
                "followers": 999999
            }
}
```
<br/>

## Dados de usuários [/USERS/FOLLOWERS/TOP5/DEL] <br/>
<b>Remover (delete) [DELETE /USERS/FOLLOWERS/TOP5/DEL]</b><br/>
Deleta um registro de usuário / seguidores.

```
+ Request (application/json)

    + Body
            {
                "username": "test_user04",
                "followers": 999999
            }


+ Response 200 (application/json)

    + Body
            {
                "mensagem": "Record deleted",
                "followers": {
                    "username": "test_user04",
                    "followers": 999999
                }
            }
```
<br/>

## Contagem de posts por data/hora [/USERS/POSTS/COUNT] <br/>
<b>Listar (list) [GET /USERS/POSTS/COUNT]</b><br/>
Cria uma lista com o total de posts por hora do dia.

```
+ Request (application/json)

    + Body


+ Response 200 (application/json)

    + Body
            {
                "mensagem": "Count posts by datetime",
                "dados": [
                    {
                        "created_at": "Sat, 07 Jan 2023 14:28:38 GMT",
                        "count_posts": 12
                    },
                    {
                        "created_at": "Sat, 07 Jan 2023 15:00:12 GMT",
                        "count_posts": 10
                    },
                    {
                        "created_at": "Sat, 07 Jan 2023 15:13:13 GMT",
                        "count_posts": 42
                    }
                ]
            }
```
<br/>

## Contagem de posts por data/hora [/USERS/POSTS/COUNT/CLEAN] <br/>
<b>Apagar (delete) [DELETE /USERS/POSTS/COUNT/CLEAN]</b><br/>
Apaga a lista com o total de posts por hora do dia.

```

+ Request (application/json)

    + Body


+ Response 200 (application/json)

    + Body
            {
                "mensagem": "All route data /countposts has been deleted."
            }

```
<br/>

## Total de posts para #tag por localização [/USERS/POSTS/TAGS/LOCALE] <br/>
<b>Listar (list) [GET /USERS/POSTS/TAGS/LOCALE]</b> <br/>
Cria uma lista com o total de posts para cada #tag por localização.

```
+ Request (application/json)

    + Body


+ Response 200 (application/json)
    
    + Body

            {
            "mensagem": "Total posts per #tags by user location",
            "dados": [
                {
                    "count_posts": 10,
                    "#tags": "#devops",
                    "user_location": "USA"
                },
                {
                    "count_posts": 41,
                    "#tags": "#devops",
                    "user_location": "Flutterverse"
                },
                {
                    "count_posts": 10,
                    "#tags": "#microservices",
                    "user_location": "Grand Tombeau de Nazarick"
                },
                {
                    "count_posts": 10,
                    "#tags": "#openbanking",
                    "user_location": "Melbourne"
                },
            ]
            }
```
<br/>

## Total de posts para #tag por localização [/USERS/POSTS/TAGS/LOCALE/CLEAN] <br/>
<b>Apagar (delete) [DELETE /USERS/POSTS/TAGS/LOCALE/CLEAN]</b><br/>
Apaga a lista com o total de posts para cada #tag por localização.

```

+ Request (application/json)

    + Body


+ Response 200 (application/json)

    + Body
            {
                "mensagem": "All route data /posttaglocation has been deleted."
            }

```
<br/>

## <a name="arquitetura">Arquitetura</a>
## <a name="comousar">Como usar</a>
<p>Para utilizar este projeto, será necessário que você tenha uma <a href="https://developer.twitter.com/en"> conta de desenvolvedor do Twitter</a> para poder autenticar na API.</p>

<p>Os pré-requisitos abaixo devem ser verificados e/ou instalados:</p>

| Pré-requisitos | Versão |
|---|---|
| `python` | >= 3|
| `docker-ce` | >= 5:20.10.22 |
| `docker-compose` | >= 1.25.0|

<br/>
<p>Com os pré-requisitos verificados, siga os passos abaixo:</p>

1 - Baixe o repositório via git:

```
git clone git@github.com:tnogueir4/case_twiiter.git
```

<br/>
2 - Edite o arquivo collect_tweets/config.toml e insira os dados conforme solicitado. O nome da app, keys e tokens você obtém através do <a href="https://developer.twitter.com/en"> portal de desenvolvedor Twitter:</a>

```
APP_NAME = 'you_app_name'
API_KEY = 'you_api_key'
API_KEY_SECRET = 'you_api_key_secret'
ACCESS_TOKEN = 'you_token'
ACCESS_TOKEN_SECRET = 'you_token_secret'
```

<br/>
3 - Suba o ambiente completo através do docker-compose na raiz do projeto:

```
$ docker-compose up -d
```
Aguarde até que todos builds das imagens sejam concluídos e cada container seja criado.

<br/>
4 - Verifique se os containers foram inicializados corretamente:

```
$ docker-compose ps
```

<br/>
5 - Caso algum container esteja com erro, verifique os logs para identificar o motivo:

```
$ docker-compose logs nome_do_container
```

<br/>
6 - Subindo os containers e não havendo mais erros, seu ambiente já estará UP e a API já poderá ser consumida, bem como verificar os logs e monitoramento.


## <a name="logs">Logs</a>
## <a name="dashboards">Dashboards</a>
