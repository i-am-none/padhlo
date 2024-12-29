# backend/app/core/init_db.py
from app.core.database import engine, metadata

metadata.create_all(engine)
