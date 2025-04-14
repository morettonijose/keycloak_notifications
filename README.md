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

git clone https://github.com/morettonijose/keycloak_notifications.git
cd mvp_2025_pos-notifications

####  2 ) Configure as variáveis de ambiente

Crie um arquivo .env ou .local.env e defina:

KEYCLOAK_URL=http://localhost:8080/
KEYCLOAK_REALM=mvp-2025
KEYCLOAK_CLIENT_ID=client_id
KEYCLOAK_CLIENT_SECRET=client_secret
KEYCLOAK_TOKEN_URL_PUBLIC=http://localhost:8080/realms/mvp-2025/protocol/openid-connect/token
DATABASE_URL=postgresql://user:password@db-notifications:5432/notifications


 ####  3 ) Suba o ambiente com Docker Compose

 docker-compose up --build

 Isso irá iniciar:

API de Notificações

API de Usuários

Banco de Dados PostgreSQL (para usuários e notificações)

Keycloak Server


 ####  4 ) Acesse

API Notifications Swagger: http://localhost:8001/docs

API Users Swagger: http://localhost:8000/docs

Keycloak Admin Console: http://localhost:8080/


 ####  Obs ) Docker

O projeto já contém:

Dockerfile para cada API

docker-compose.yml para orquestração dos serviços

Suba o ambiente rodando : docker-compose up --build
