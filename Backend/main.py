# backend/main.py
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from app.routes import user
from app.auth import create_access_token, decode_access_token
from app.core.database import database

app = FastAPI()

# OAuth2 scheme for token authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Personalized Learning Assistant API!"}

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# Secure endpoint example
@app.get("/secure")
def secure_endpoint(token: str = Depends(oauth2_scheme)):
    user = decode_access_token(token)
    return {"message": f"Welcome, {user['username']}!"}

# Include user routes
app.include_router(user.router, prefix="/api/v1", tags=["User"])

# Include authentication routes
from app.auth.auth import auth_router
app.include_router(auth_router, prefix="/api/v1/auth", tags=["Auth"])

# Social authentication (Google, GitHub)
from app.auth.social_auth import social_auth_router
app.include_router(social_auth_router, prefix="/api/v1/auth/social", tags=["Social Auth"])
