# MVP 2025 POS - API Notifications

Esta API é um dos componentes do sistema MVP 2025 POS, e se comunica com o serviço de gerenciamento de usuários (api-users).

API REST desenvolvida em FastAPI para gerenciamento de notificações, integrada com Keycloak para autenticação .


##  Funcionalidades

### Autenticação OAuth2 via Keycloak.

#### CRUD de Notificações:

POST /notification: Criar uma nova notificação

GET /notification/{user_id}: Listar notificações de um usuário

PUT /notification/{notification_id}: Atualizar uma notificação

DELETE /notification/{notification_id}: Deletar uma notificação


# Instalação e Configuração

####  1 ) Clone o projeto

```
git clone https://github.com/morettonijose/keycloak_notifications.git
cd keycloak_notifications
```

####  2 ) Configure as variáveis de ambiente

Crie um arquivo .env ou .local.env e defina:

```
KEYCLOAK_URL=http://localhost:8080/
KEYCLOAK_REALM=mvp-2025
KEYCLOAK_CLIENT_ID=client_id
KEYCLOAK_CLIENT_SECRET=client_secret
KEYCLOAK_TOKEN_URL_PUBLIC=http://localhost:8080/realms/mvp-2025/protocol/openid-connect/token
DATABASE_URL=postgresql://user:password@db-notifications:5432/notifications
```



####  3 ) Copie os arquivos docker-compose.yml , docker-compose.override.yml , Dockerfile para a pasta raiz do projeto  e retorne para a pasta raiz do projeto

```
cd ../
```


 ####  4 ) Suba o ambiente com Docker Compose

```
 docker-compose up --build
 ```

 Isso irá iniciar:

API de Notificações

API de Usuários

Banco de Dados PostgreSQL (para usuários e notificações)

Keycloak Server


 ####  5 ) Acesse

Keycloak Admin Console: http://localhost:8080/

API Notifications Swagger: http://localhost:8001/docs

API Users Swagger: http://localhost:8000/docs



 ####  6 ) Docker

O projeto já contém:

Dockerfile para cada API e docker-compose.yml para orquestração dos serviços . Caso você altere o nome das pastas dos repositórios baixados, lembre de alterar o destino do build dos componentes no arquivo docker-compose.yml

Suba o ambiente rodando : docker-compose up --build


 ####  7 ) Configurando o KeyCloak : 

 
7.1 ) Faça o login no admin do keycloak : http://localhost:8080/admin

7.2 ) Crie o ‘realm’ (tenant)  (grupos de usuários) : general ; 

7.3 ) Crie um cliente para a aplicação : escolha o nome client1 ; 

7.4 ) Crie o usuários que terão acesso : user1 ; 


Obs : caso você escolha um  realm ou nome de cliente  diferente , lembre de alterar o arquivo .local.env ; 