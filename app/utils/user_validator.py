import requests
from fastapi import HTTPException

USERS_API_BASE_URL = "http://api-users:8000"

def validate_user_id(user_id: int, token: str):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{USERS_API_BASE_URL}/user/{user_id}", headers=headers)

    if response.status_code == 404:
        raise HTTPException(status_code=400, detail="User ID not found")
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Failed to validate user ID")
