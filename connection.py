from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

engine = create_engine("sqlite:///storage.db")
Base = declarative_base()