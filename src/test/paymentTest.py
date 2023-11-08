
import sys
import pytest
sys.path.append("..")
from controller.paymentManager import PaymentManager
# assuming the class is in payment_manager.py

# Fixture to create a PaymentManager instance


@pytest.fixture
def payment_manager():
    return PaymentManager()

def test_valid_credit_card_1(payment_manager):
    credit_card_info = ["Debit", 1234567890123456, "01/24", 100]
    assert payment_manager.processPayment(credit_card_info) == True

def test_invalid_card_number_too_large(payment_manager):
    credit_card_info = ["Debit", 12345678901234567, "01/24", 100]
    assert payment_manager.processPayment(credit_card_info) == False

def test_invalid_card_number_too_small(payment_manager):
    credit_card_info = ["Debit", 12345678901234, "01/24", 100]
    assert payment_manager.processPayment(credit_card_info) == False

def test_valid_credit_card_2(payment_manager):
    credit_card_info = ["Debit", 1234567890123456, "01/24", 1000]
    assert payment_manager.processPayment(credit_card_info) == True

def test_invalid_security_code_too_large(payment_manager):
    credit_card_info = ["Debit", 1234567890123456, "01/24", 10000]
    assert payment_manager.processPayment(credit_card_info) == False

def test_invalid_security_code_too_small(payment_manager):
    credit_card_info = ["Debit", 1234567890123456, "01/24", 99]
    assert payment_manager.processPayment(credit_card_info) == False

def test_valid_credit_card_3(payment_manager):
    credit_card_info = ["Debit", 1234567890123456, "12/24", 100]
    assert payment_manager.processPayment(credit_card_info) == True

def test_invalid_expiry_date_month_too_low(payment_manager):
    credit_card_info = ["Debit", 1234567890123456, "0/25", 100]
    assert payment_manager.processPayment(credit_card_info) == False

def test_invalid_expiry_date_month_too_high(payment_manager):
    credit_card_info = ["Debit", 1234567890123456, "13/25", 100]
    assert payment_manager.processPayment(credit_card_info) == False

def test_invalid_expiry_date_month_at_end_of_year(payment_manager):
    credit_card_info = ["Debit", 1234567890123456, "12/23", 100]
    assert payment_manager.processPayment(credit_card_info) == False