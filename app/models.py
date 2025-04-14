from sqlalchemy import Column, Integer, String
from app.database import Base

class Notification(Base):
    __tablename__ = "notifications"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    title = Column(String, index=True)
    message = Column(String)
    keycloak_userid = Column(String, index=True, nullable=False, default="")  
    status = Column(String, index=True, default="draft")   
