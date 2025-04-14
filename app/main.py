from fastapi import FastAPI, Depends, HTTPException, Security
from fastapi.openapi.utils import get_openapi
from app import models, schemas, crud, database, auth
from sqlalchemy.orm import Session
import os
from dotenv import load_dotenv

from app.utils.user_validator import validate_user_id


load_dotenv()

CLIENT_ID = os.getenv("KEYCLOAK_CLIENT_ID")
CLIENT_SECRET = os.getenv("KEYCLOAK_CLIENT_SECRET")
TOKEN_URL = os.getenv("KEYCLOAK_TOKEN_URL_PUBLIC")

app = FastAPI(
    title="MVP 2025 POS - API Notifications",
    version="1.0.0",
    description="API for Notification Management",
    openapi_tags=[{"name": "notifications", "description": "Notification operations"}],
    swagger_ui_init_oauth={
        "clientId": CLIENT_ID,
        "clientSecret": CLIENT_SECRET,
        "usePkceWithAuthorizationCodeGrant": False,
    },
    dependencies=[Security(auth.verify_token)]  # 🔒 Protege todas as rotas automaticamente
)

models.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/notification", response_model=schemas.Notification)
def create_notification(
    notification: schemas.NotificationCreate,
    db: Session = Depends(get_db),
    token: str = Security(auth.verify_token)
):
    keycloak_userid = auth.get_keycloak_user_id(token)

    validate_user_id(notification.user_id , token )  #Verifica se user_id existe via api-users

    return crud.create_notification(db=db, notification=notification, keycloak_user_id=keycloak_userid)

@app.get("/notification/{user_id}", response_model=list[schemas.Notification])
def read_notifications(user_id: int, db: Session = Depends(get_db)):
    return crud.get_notifications_by_user(db, user_id=user_id)

@app.put("/notification/{notification_id}", response_model=schemas.Notification)
def update_notification(
    notification_id: int,
    notification: schemas.NotificationUpdate,
    db: Session = Depends(get_db),
    token: str = Security(auth.verify_token)  
):
    keycloak_userid = auth.get_keycloak_user_id(token)  

    validate_user_id(notification.user_id , token )  #Verifica se user_id existe via api-users

    return crud.update_notification(
        db=db,
        notification_id=notification_id,
        notification=notification,
        keycloak_user_id=keycloak_userid   
    )




@app.delete("/notification/{notification_id}")
def delete_notification(notification_id: int, db: Session = Depends(get_db)):
    return crud.delete_notification(db=db, notification_id=notification_id)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="MVP 2025 POS - API Notifications",
        version="1.0.0",
        description="API for Notification Management",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "OAuth2PasswordBearer": {
            "type": "oauth2",
            "flows": {
                "password": {
                    "tokenUrl": TOKEN_URL,
                    "scopes": {}
                }
            }
        }
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
