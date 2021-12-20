import sqlite3
from sqlalchemy import Integer, String, Column, ForeignKeyConstraint
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

engine = create_engine("sqlite:///storage.db")
Base = declarative_base()