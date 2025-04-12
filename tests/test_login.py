
import pytest
from login import login_check 

class TestLogin:

    def test_login_success(self, valid_user):
        username = valid_user["username"]
        password = valid_user["password"]
        assert login_check(username, password) == True

    def test_login_fail_invalid_username(self, invalid_user):
        username = invalid_user["username"]
        password = invalid_user["password"]
        assert login_check(username, password) == False

    def test_login_fail_empty_input(self):
        assert login_check("", "") == False