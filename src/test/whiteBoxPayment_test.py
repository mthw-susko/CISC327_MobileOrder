
import sys
import pytest
sys.path.append("..")
from controller.paymentManager import PaymentManager

@pytest.fixture
def payment_manager():
    return PaymentManager()

#  no credit card
def test_no_credit_card_number(payment_manager):
    credit_card_info = ["Debit", 1234567890123456, "01/24", 100]
    assert payment_manager.processPayment(credit_card_info) == True

def test_invalid_credit_card_number(payment_manager):
    credit_card_info = ["Debit", "", "01/24", 100]
    assert payment_manager.processPayment(credit_card_info) == False

# card number validation
def test_valid_credit_card_1(payment_manager):
    credit_card_info = ["Debit", 1234567890123456, "01/24", 100]
    assert payment_manager.processPayment(credit_card_info) == True

def test_invalid_card_number_too_large(payment_manager):
    credit_card_info = ["Debit", 12345678901234567, "01/24", 100]
    assert payment_manager.processPayment(credit_card_info) == False

# expiry month invalid (too small)
def test_valid_credit_card_month_1(payment_manager):
    credit_card_info = ["Debit", 1234567890123456, "01/24", 100]
    assert payment_manager.processPayment(credit_card_info) == True

def test_invalid_credit_card_month_too_small(payment_manager):
    credit_card_info = ["Debit", 1234567890123456, "00/24", 100]
    assert payment_manager.processPayment(credit_card_info) == False

# expiry year invalid (too large)
def test_valid_credit_card_month_2(payment_manager):
    credit_card_info = ["Debit", 1234567890123456, "01/24", 100]
    assert payment_manager.processPayment(credit_card_info) == True

def test_invalid_credit_card_month_too_large(payment_manager):
    credit_card_info = ["Debit", 1234567890123456, "13/24", 100]
    assert payment_manager.processPayment(credit_card_info) == False

# expiry at end of year
def test_valid_credit_card_year(payment_manager):
    credit_card_info = ["Debit", 1234567890123456, "01/24", 100]
    assert payment_manager.processPayment(credit_card_info) == True

def test_invalid_credit_card_month_at_year_end(payment_manager):
    credit_card_info = ["Debit", 1234567890123456, "12/23", 100]
    assert payment_manager.processPayment(credit_card_info) == False

# expiry format not valid
def test_valid_credit_card_year(payment_manager):
    credit_card_info = ["Debit", 1234567890123456, "01/24", 100]
    assert payment_manager.processPayment(credit_card_info) == True

def test_invalid_credit_card_month_at_year_end(payment_manager):
    credit_card_info = ["Debit", 1234567890123456, "12/23", 100]
    assert payment_manager.processPayment(credit_card_info) == False

# no security code
def test_valid_credit_card_security_code(payment_manager):
    credit_card_info = ["Debit", 1234567890123456, "01/24", 100]
    assert payment_manager.processPayment(credit_card_info) == True

def test_invalid_credit_card_no_security_code(payment_manager):
    credit_card_info = ["Debit", 1234567890123456, "12/23", ""]
    assert payment_manager.processPayment(credit_card_info) == False

# security code invalid
def test_valid_credit_card_security_code_1(payment_manager):
    credit_card_info = ["Debit", 1234567890123456, "01/24", 100]
    assert payment_manager.processPayment(credit_card_info) == True

def test_invalid_credit_card_no_security_code(payment_manager):
    credit_card_info = ["Debit", 1234567890123456, "12/23", 1000]
    assert payment_manager.processPayment(credit_card_info) == False

# if everything else is valid, then should print success
def test_valid_all_credit_card_info(capsys, payment_manager):
    credit_card_info = ["Debit", 1234567890123456, "01/24", 100]
    payment_manager.processPayment(credit_card_info)
    captured = capsys.readouterr()
    assert "Payment Processed!" in captured.out

def test_not_valid_all_credit_card_info(capsys, payment_manager):
    credit_card_info = ["Debit", 1234567890123456, "01/24", 100]
    payment_manager.processPayment(credit_card_info)
    captured = capsys.readouterr()
    assert "" in captured.out
