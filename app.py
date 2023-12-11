# main.py
from fastapi import FastAPI, HTTPException

app = FastAPI()

# Simulated data store
users = [{"id": 1, "name": "John Doe"}, {"id": 2, "name": "Jane Doe"}]

@app.get("/users")
def read_users():
    return users

@app.post("/users")
def add_user(user_id: int, name: str):
    # Intentional issue: Lack of data validation and proper request body handling
    new_user = {"id": user_id, "name": name}
    users.append(new_user)
    return new_user

@app.get("/users/{user_id}")
def read_user(user_id: int):
    # Intentional issue: Inefficient user lookup
    for user in users:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")
