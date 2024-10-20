
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from models import engine, Product, CartItems, Order, OrderItem


Session = sessionmaker(bind=engine)
session = Session()

products = [
    Product(name='Laptop', price=1200.99, quantity_in_stock=50),
    Product(name='Smartphone', price=699.49, quantity_in_stock=150),
    Product(name='Headphones', price=99.99, quantity_in_stock=200),
    Product(name='Smartwatch', price=199.99, quantity_in_stock=75)
]
session.add_all(products)
session.commit()

cart_items = [
    CartItems(product_id=1, quantity=2),
    CartItems(product_id=3, quantity=3),
    CartItems(product_id=2, quantity=1)
]
session.add_all(cart_items)
session.commit()

orders = [
    Order(order_date=datetime(2024, 10, 19, 14, 0, 0), total_amount=2300.47)
]
session.add_all(orders)
session.commit()

order_items = [
    OrderItem(order_id=1, product_id=1, quantity=2, price_per_item=1200.99),
    OrderItem(order_id=1, product_id=3, quantity=3, price_per_item=99.99),
    OrderItem(order_id=1, product_id=2, quantity=1, price_per_item=699.49)
]
session.add_all(order_items)
session.commit()

session.close()
