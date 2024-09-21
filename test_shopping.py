import unittest
from shoppingCart import ShoppingCart

class TestShopping(unittest.TestCase):
    
    def test_add_item(self):
        cart = ShoppingCart()
        cart.add_item('Mobile', 100, 1)
        self.assertEqual(cart.total_price(), 100)
        self.assertEqual(cart.items[0]['name'], 'Mobile')
        self.assertEqual(cart.items[0]['price'], 100)
        self.assertEqual(cart.items[0]['quantity'], 1)
        
    def test_total_price(self):
        cart = ShoppingCart()
        cart.add_item('Mobile', 100, 1)
        self.assertEqual(cart.total_price(), 100)
        
    def test_remove_item(self):
        cart = ShoppingCart()
        cart.add_item('Mobile', 100, 1)
        cart.remove_item('Mobile')
        self.assertTrue(cart.is_empty())
        
    def test_is_empty(self):
        cart = ShoppingCart()
        self.assertTrue(cart.is_empty())
        cart.add_item('Mobile', 100, 1)
        cart.remove_item('Mobile')
        self.assertTrue(cart.is_empty())
        
    def test_add_multiple_items(self):
        cart = ShoppingCart()
        cart.add_item('Mobile', 100, 2)
        cart.add_item('Laptop', 300, 4)
        self.assertEqual(cart.total_price(), 1400)
        self.assertEqual(len(cart.items), 2)
        
    def test_remove_nonexistent_item(self):
        cart = ShoppingCart()
        cart.add_item('Mobile', 100, 1)
        cart.add_item('Laptop', 200, 2)
        cart.remove_item('Laptop')
        self.assertEqual(len(cart.items), 1)
        self.assertEqual(cart.items[0]['name'], 'Mobile')
        
if __name__ == '__main__':
    unittest.main()