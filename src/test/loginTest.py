
import sys
import pytest
sys.path.append("..")
from view.mainView import MainView

@pytest.fixture
def main_view():
    return MainView()

def test_valid_login(main_view):
    username = "Bobross1"
    email = "bobross1@hotmail.com"
    password = "Bobross2"
    assert main_view.validateLogin(username, email, password) == True

def test_invalid_login_taken_username(main_view):
    username = "Jabezng1"
    email = "bobross1@hotmail.com"
    password = "Bobross2"
    assert main_view.validateLogin(username, email, password) == False

def test_invalid_login_bad_email(main_view):
    username = "Bobross1"
    email = "bobross1hotmail.com"
    password = "Bobross2"
    assert main_view.validateLogin(username, email, password) == False

def test_invalid_login_bad_password_1(main_view):
    username = "Bobross1"
    email = "bobross1@hotmail.com"
    password = "bobross2"
    assert main_view.validateLogin(username, email, password) == False

def test_invalid_login_bad_password_2(main_view):
    username = "Bobross1"
    email = "bobross1@hotmail.com"
    password = "BOBROSS2"
    assert main_view.validateLogin(username, email, password) == False

def test_invalid_login_bad_password_3(main_view):
    username = "Bobross1"
    email = "bobross1@hotmail.com"
    password = "Bobross"
    assert main_view.validateLogin(username, email, password) == False

def test_invalid_login_no_username(main_view):
    username = ""
    email = "bobross1@hotmail.com"
    password = "Bobross"
    assert main_view.validateLogin(username, email, password) == False

def test_invalid_login_no_email(main_view):
    username = "Bobross1"
    email = ""
    password = "Bobross"
    assert main_view.validateLogin(username, email, password) == False

def test_invalid_login_no_password(main_view):
    username = "Bobross1"
    email = "bobross1@hotmail.com"
    password = ""
    assert main_view.validateLogin(username, email, password) == False
