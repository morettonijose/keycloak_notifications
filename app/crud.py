from sqlalchemy.orm import Session
from app import models, schemas

def create_notification(db: Session, notification: schemas.NotificationCreate, keycloak_user_id: str):
    db_notification = models.Notification(
        user_id=notification.user_id,
        title=notification.title,
        message=notification.message,
        status=notification.status,   
        keycloak_userid=keycloak_user_id   
    )
    db.add(db_notification)
    db.commit()
    db.refresh(db_notification)
    return db_notification

def get_notifications_by_user(db: Session, user_id: int):
    return db.query(models.Notification).filter(models.Notification.user_id == user_id).all()

def update_notification(db: Session, notification_id: int, notification: schemas.NotificationUpdate, keycloak_user_id: str):
    db_notification = db.query(models.Notification).filter(models.Notification.id == notification_id).first()
    if db_notification is None:
        raise HTTPException(status_code=404, detail="Notification not found")
    
    db_notification.user_id = notification.user_id
    db_notification.title = notification.title
    db_notification.message = notification.message
    db_notification.status = notification.status
    db_notification.keycloak_userid = keycloak_user_id  # 🔥 Atualiza automático com o do token

    db.commit()
    db.refresh(db_notification)
    return db_notification



def delete_notification(db: Session, notification_id: int):
    db_notification = db.query(models.Notification).filter(models.Notification.id == notification_id).first()
    db.delete(db_notification)
    db.commit()
    return {"message": "Notification deleted"}
