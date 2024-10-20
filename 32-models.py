from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database connection
engine = create_engine('postgresql+psycopg2://postgres:Tika2018@localhost:5432/postgres_py')
Base = declarative_base()

# Define the Book class
class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    author = Column(String(100), nullable=False)
    release_year = Column(Integer, nullable=False)
    isbn = Column(String(13), unique=True, nullable=False)

# Create the table in the database
Base.metadata.create_all(engine)

# Session setup
Session = sessionmaker(bind=engine)
session = Session()

