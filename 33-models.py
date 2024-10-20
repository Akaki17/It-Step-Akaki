from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

host = 'localhost'
port = 5432
### createdb postgres_py ##ვერ ავამუშავე ბრძანება და შევეშვი. არსებულ database გავუშვი ინფორმაცია
database = 'postgresdb1'
user = 'postgres'
password = 'Tika2018'

engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}')
Base = declarative_base()

class Product(Base):
    __tablename__ = 'product'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(50), nullable=False)
    price = Column('Price', Float, nullable=False)
    quantity_in_stock = Column('quantity_in_stock', Integer, nullable=False)
    

class CartItems(Base):
    __tablename__ = 'cart_items'
    
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    product_id = Column('product_id', Integer, ForeignKey('product.id'), nullable=False)
    quantity = Column('quantity', Integer, nullable=False)
    
class Order(Base):
    __tablename__ = 'order'
    
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    order_date = Column('order_date', DateTime, nullable=True)
    total_amount = Column('total_amount', Float, nullable=False)
    
class OrderItem(Base):
    __tablename__ = 'order_item'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    order_id = Column('order_id', Integer, ForeignKey('order.id'), nullable=False)
    product_id = Column('product_id', Integer, ForeignKey('product.id'), nullable=False)
    quantity = Column('quantity', Integer, nullable=False)
    price_per_item = Column('price_per_item', Float, nullable=False)

Base.metadata.create_all(engine)
