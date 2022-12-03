import pytest
import sys

@pytest.mark.parametrize("username,password",
                         [
                             ("us1","pw1"),
                             ("us2","pw2"),
                             ("us3","pw3"),
                             ("us4","pw4")
                         ])
def test_login(username, password):
    print(username)
    print(password)