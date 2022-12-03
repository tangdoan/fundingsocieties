import pytest
import sys

@pytest.mark.skip
def test_login():
    print("Login success")

@pytest.mark.skipif(sys.version_info<(3,8), reason="Not compatible version")
def test_addProduct():
    print("Added product success")

@pytest.mark.xfail
def test_logout():
    assert False
    print("Logout success")

def test_exit():
    assert True
    print("Exit success")