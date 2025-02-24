from sqlalchemy import Column, Integer, String, Float
from .database import engine, SessionLocal
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, index=True)
    price = Column(Float)
    quantity = Column(Integer)
    order_type = Column(String)

def init_db():
    Base.metadata.create_all(bind=engine)
