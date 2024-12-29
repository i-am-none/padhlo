# backend/app/models/user.py
from sqlalchemy import Table, Column, Integer, String
from app.core.database import metadata

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(50), nullable=False),
    Column("email", String(120), unique=True, nullable=False),
    Column("hashed_password", String, nullable=False),
)
