from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Update with your PostgreSQL connection info
DATABASE_URL = "postgresql://postgres:PostPmDh20@localhost/order_db"

# Set up engine and base
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)

# Main execution
# if __name__ == "__main__":
#     print("Connecting to database...")
#     Base.metadata.create_all(bind=engine)
#     print("Table 'Users' created successfully (if it didn't already exist).")