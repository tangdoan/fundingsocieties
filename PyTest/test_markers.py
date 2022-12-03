import pytest

@pytest.mark.smoke
def test_login():
    print("Login success")
@pytest.mark.regression
def test_addProduct():
    print("Added product success")
@pytest.mark.smoke
def test_logout():
    print("Logout success")