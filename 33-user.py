from models import engine, Product, CartItems, Order, OrderItem
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Session = sessionmaker(bind=engine)
session = Session()

def view_cart():
    cart_items = session.query(CartItems).all()
    for item in cart_items:
        product = session.query(Product).filter(Product.id == item.product_id).first()
        print(f"Product: {product.name}, Quantity: {item.quantity}, Total: ${product.price * item.quantity:.2f}")

def add_to_cart():
    product_id = int(input("Enter the product ID to add to the cart: "))
    quantity = int(input("Enter the quantity: "))
    new_item = CartItems(product_id=product_id, quantity=quantity)
    session.add(new_item)
    session.commit()
    print("Product added to the cart!")

def remove_from_cart():
    product_id = int(input("Enter the product ID to remove from the cart: "))
    cart_item = session.query(CartItems).filter(CartItems.product_id == product_id).first()
    if cart_item:
        session.delete(cart_item)
        session.commit()
        print("Product removed from the cart!")
    else:
        print("Product not found in the cart.")

def execute_order():
    cart_items = session.query(CartItems).all()
    if not cart_items:
        print("Your cart is empty!")
        return
    total_amount = sum(item.quantity * session.query(Product).filter(Product.id == item.product_id).first().price for item in cart_items)
    new_order = Order(order_date=datetime.now(), total_amount=total_amount)
    session.add(new_order)
    session.commit()
    for item in cart_items:
        new_order_item = OrderItem(order_id=new_order.id, product_id=item.product_id, quantity=item.quantity, price_per_item=session.query(Product).filter(Product.id == item.product_id).first().price)
        session.add(new_order_item)
    session.commit()
    session.query(CartItems).delete()
    session.commit()
    print(f"Order executed! Total amount: ${total_amount:.2f}")

def view_orders():
    orders = session.query(Order).all()
    for order in orders:
        print(f"Order ID: {order.id}, Date: {order.order_date}, Total Amount: ${order.total_amount:.2f}")

def main_menu():
    while True:
        print("\n1. View cart")
        print("2. Add products to the cart")
        print("3. Remove products from the cart")
        print("4. Execute order")
        print("5. View orders")
        print("6. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            view_cart()
        elif choice == '2':
            add_to_cart()
        elif choice == '3':
            remove_from_cart()
        elif choice == '4':
            execute_order()
        elif choice == '5':
            view_orders()
        elif choice == '6':
            session.close()
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    main_menu()
