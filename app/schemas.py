from typing import Optional
from pydantic import BaseModel

class NotificationBase(BaseModel):
    user_id: int
    title: str
    message: str

class NotificationCreate(NotificationBase):
    keycloak_userid: Optional[str] = None
    status: Optional[str] = None

class NotificationUpdate(NotificationBase):
    user_id: int
    title: str
    message: str
    status: Optional[str] = None

class Notification(NotificationBase):
    id: int
    keycloak_userid: Optional[str] = None
    status: Optional[str] = None

    class Config:
        from_attributes = True   