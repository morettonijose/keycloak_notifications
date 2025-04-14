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



 ###  6 ) Docker

O projeto já contém:

Dockerfile para cada API e docker-compose.yml para orquestração dos serviços . Caso você altere o nome das pastas dos repositórios baixados, lembre de alterar o destino do build dos componentes no arquivo docker-compose.yml

Suba o ambiente rodando : docker-compose up --build


 ### 7 ) Configurando o KeyCloak : 

 
 #### 7.1 ) Faça o login no admin do keycloak : http://localhost:8080/admin

 #### 7.2 ) Crie o ‘realm’ (tenant)  (grupos de usuários) : 
         - Na opção "Realm name" digite o nome : general ; 

 #### 7.3 ) Crie um cliente para a aplicação : 
        - Na opção Cliente ID digite client1 ; 
        - Marque as opções : 
            - Client authentication : ON  
           -  Valid redirect URIs  (adicione as 3 opções abaixo)
                    - *
                    - http://localhost:8000/*
                    - http://localhost:8001/*
           -  Web origins   (adicione as 3 opções abaixo)
                    - *
                    - http://localhost:8000
                    - http://localhost:8001
            - Standard flow :  marcado
            - Direct access grants : marcado
        - Na Aba Credential copie seu Secret Key e edite  a chave dos arquivos 
        .local.env  de cada um  dos 2 componentes.




 #### 7.4 ) Crie o usuários que terão acesso : user1 ; 
          - Adicione um novo usuário , marque a opção email verificado ;
          - Na aba Credential crie uma senha para o usuário e desmarque "Tempporary" para que fique na posição OFF  ; 


 #### 7.5 )  caso você escolha um  realm  ou nome de client  diferente , lembre de alterar  também o arquivo .local.env ; 

 #### 7.6 ) Depois de alterar seu arquivo .env.local lembre de reiniciar o projeto e  dar um novo build 

```
 docker-compose up --build
 ```


 ### 8 ) Resolução de erros prováveis : 

 #### Erro ao Autorizar a API no botão Authorize : auth errorTypeError: Failed to fetch

 #### 8.1) Verifique o Client Scope  e Mappers :

 Acesse Client-> client1 -> Client Scopes ; 

 Clique em client1-dedicated e acesse a aba Mappers  ; 

 Configure um novo Mapper ; 
 - Mapper type : Audience ; 
   Name : audience ; 
   Include Client : cliente1 ; 



 

