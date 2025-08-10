from sqlalchemy import create_engine
from models import Base

# Create SQLite database
engine = create_engine('sqlite:///lms.db')

# Create all tables
Base.metadata.create_all(engine)

print("✅ Database tables created successfully!")
