# backend/app/core/database.py
from databases import Database
from sqlalchemy import create_engine, MetaData

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Create database instance
database = Database(DATABASE_URL)

# SQLAlchemy engine (if needed for ORM usage)
engine = create_engine(DATABASE_URL)

# Metadata for table definitions
metadata = MetaData()
