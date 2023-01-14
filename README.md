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
 - [Architecture](#architecture)
 - [How_to](#howto)
 - [Logs](#logs)
 - [Dashboards](#dashboards)
<!--te-->

## <a name="apis">APIs</a>
O projeto Case_twiiter disponibiliza uma API REST que permite o consumo de alguns dados extraidos das API´s do Twitter.

Recursos disponíveis via API:
 * Top 5 usuários com mais seguidores.
 * Total de posts, agrupadas por hora do dia independente da #tag.
 * Total de posts para cada uma das #tags por localização do usuário que postou.

 ## Métodos
Requisições para a API devem seguir os padrões:
| Método | Descrição |
|---|---|
| `GET` | Retorna informações de um ou mais registros. |
| `POST` | Utilizado para criar um novo registro. |
| `DELETE` | Remove um ou mais registros. |

## Respostas

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

## Recursos

### Dados de usuários [/topfollowers] <br/>
<b>Listar (list) [GET /topfollowers]</b>
Cria uma lista com os 5 usuários com mais seguidores.

+ Request (application/json)

    + Body

<br/>

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

<br/><br/>

<b>Novo (create) [POST /topfollowers]</b>
Inclui um novo registro de usuário / seguidores.

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

<br/><br/>

<b>Remover (delete) [DELETE /topfollowers]</b>
Deleta um registro de usuário / seguidores.

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

## <a name="architecture">Architecture</a>
## <a name="howto">How to</a>
## <a name="logs">Logs</a>
## <a name="dashboards">Dashboards</a>
