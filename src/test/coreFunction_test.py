import sys
import pytest
sys.path.append("..")
from view.mainView import MainView
from view.orderView import OrderView
from controller.paymentManager import PaymentManager


@pytest.fixture
def main_view():
    return MainView()

@pytest.fixture
def order_view():
    return OrderView(None, None, None, None)

@pytest.fixture
def payment_manager():
    return PaymentManager()

# login tests
def test_valid_login(capsys, main_view):
    username = "Matthewsusko2"
    password = "Hello101"

    main_view.tryLogin(username, password)
    captured = capsys.readouterr()
    assert "Successful login" in captured.out


def test_invalid_login_no_username(capsys, main_view):
    username = "Matthewsusko3"
    password = "Hello101"
    main_view.tryLogin(username, password)
    captured = capsys.readouterr()
    assert "Username does not exist" in captured.out

def test_invalid_login_bad_password(capsys, main_view):
    username = "Matthewsusko2"
    password = "Hello102"
    main_view.tryLogin(username, password)
    captured = capsys.readouterr()
    assert "Incorrect Password" in captured.out

# register tests
def test_valid_register(capsys, main_view):
    username = "bobross"
    email = "test@test.com"
    password = "Hello103"
    main_view.validateLogin(username, email, password)
    captured = capsys.readouterr()
    assert "User Registered Successfully" in captured.out

def test_invalid_register_no_number(capsys, main_view):
    username = "bobross"
    email = "test@test.com"
    password = "Hello"

    main_view.validateLogin(username, email, password)
    captured = capsys.readouterr()
    assert "Password must contain at least one number" in captured.out

def test_invalid_register_no_lowercase(capsys, main_view):
    username = "bobross"
    email = "test@test.com"
    password = "HELLO103"

    main_view.validateLogin(username, email, password)
    captured = capsys.readouterr()
    assert "Password must contain at least one lowercase letter" in captured.out

def test_invalid_register_no_uppercase(capsys, main_view):
    username = "bobross"
    email = "test@test.com"
    password = "hello103"

    main_view.validateLogin(username, email, password)
    captured = capsys.readouterr()
    assert "Password must contain at least one uppercase letter" in captured.out

def test_invalid_register_bad_email(capsys, main_view):
    username = "bobross"
    email = "testtest.com"
    password = "Hello103"

    main_view.validateLogin(username, email, password)
    captured = capsys.readouterr()
    assert "Invalid email entered" in captured.out

def test_invalid_register_taken_username(capsys, main_view):
    username = "Matthewsusko2"
    email = "test@test.com"
    password = "Hello103"

    main_view.validateLogin(username, email, password)
    captured = capsys.readouterr()
    assert "Username has been taken" in captured.out

def test_invalid_register_missing_password(capsys, main_view):
    username = "Matthewsusko2"
    email = "test@test.com"
    password = ""

    main_view.validateLogin(username, email, password)
    captured = capsys.readouterr()
    assert "Missing password" in captured.out

def test_invalid_register_missing_email(capsys, main_view):
    username = "Matthewsusko2"
    email = ""
    password = "Hello3"

    main_view.validateLogin(username, email, password)
    captured = capsys.readouterr()
    assert "Missing password" in captured.out

def test_invalid_register_missing_email(capsys, main_view):
    username = ""
    email = "test@test.com"
    password = "Hello3"

    main_view.validateLogin(username, email, password)
    captured = capsys.readouterr()
    assert "Missing username" in captured.out


# order tests
def test_successful_checkout(capsys, order_view):
    order_view.submitOrder(True)
    captured = capsys.readouterr()
    assert "Order Submitted!" in captured.out

def test_empty_cart(capsys, order_view):
    order_view.cartEmpty([])
    captured = capsys.readouterr()
    assert "Your cart is empty" in captured.out

def test_empty_cart(capsys, order_view):
    order_view.cartEmpty([])
    captured = capsys.readouterr()
    assert "Your cart is empty" in captured.out

def test_order_delivered(capsys, order_view):
    order_view.orderDelivered(0)
    captured = capsys.readouterr()
    assert "Order Delivered!" in captured.out

def test_order_delivering(capsys, order_view):
    order_view.orderDelivered(10)
    captured = capsys.readouterr()
    assert "Delivery on its way!" in captured.out

def test_valid_credit_card(payment_manager,capsys):
    credit_card_info = ["Debit", 1234567890123456, "01/24", 100]    
    payment_manager.processPayment(credit_card_info)
    captured = capsys.readouterr()
    assert "Payment processed successfully." in captured.out

def test_invalid_card_number_too_large(payment_manager, capsys):
    credit_card_info = ["Debit", 12345678901234567, "01/24", 100]
    payment_manager.processPayment(credit_card_info)
    captured = capsys.readouterr()
    assert "Your card number is invalid" in captured.out

def test_invalid_card_number_too_small(payment_manager, capsys):
    credit_card_info = ["Debit", 12345678901234, "01/24", 100]
    payment_manager.processPayment(credit_card_info)
    captured = capsys.readouterr()
    assert "Your card number is invalid" in captured.out

def test_invalid_security_code_too_large(payment_manager, capsys):
    credit_card_info = ["Debit", 1234567890123456, "01/24", 10000]
    payment_manager.processPayment(credit_card_info)
    captured = capsys.readouterr()
    assert "Security code is invalid" in captured.out

def test_invalid_security_code_too_small(payment_manager, capsys):
    credit_card_info = ["Debit", 1234567890123456, "01/24", 99]
    payment_manager.processPayment(credit_card_info)
    captured = capsys.readouterr()
    assert "Security code is invalid" in captured.out

def test_invalid_expiry_date_month_too_low(payment_manager, capsys):
    credit_card_info = ["Debit", 1234567890123456, "0/25", 100]
    payment_manager.processPayment(credit_card_info)
    captured = capsys.readouterr()
    assert "Your card's expiration date is invalid" in captured.out

def test_invalid_expiry_date_month_too_high(payment_manager, capsys):
    credit_card_info = ["Debit", 1234567890123456, "13/25", 100]
    payment_manager.processPayment(credit_card_info)
    captured = capsys.readouterr()
    assert "Your card's expiration date is invalid" in captured.out

def test_invalid_expiry_date_month_at_end_of_year(payment_manager, capsys):
    credit_card_info = ["Debit", 1234567890123456, "12/23", 100]
    payment_manager.processPayment(credit_card_info)
    captured = capsys.readouterr()
    assert "Your card's expiration date is invalid" in captured.out
