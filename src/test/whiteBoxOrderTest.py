import sys
import pytest
sys.path.append("..")
from controller.orderManager import OrderManager
# assuming the class is in order_manager.py

# Fixture to create a OrderManager instance
@pytest.fixture
def order_manager():
    return OrderManager

# True Block validation
def test_valid_cart_and_order_not_submitted(order_manager):
    cart = OrderManager.cart
    is_order_submitted = False
    assert order_manager.submitOrder(cart, is_order_submitted) == True

# False block validation
def test_invalid_cart_and_order_not_submitted(order_manager):
    cart = None
    is_order_submitted = True
    assert order_manager.submitOrder(cart, is_order_submitted) == False
