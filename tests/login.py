
def login_check(username, password):
    valid_credentials = {"testuser": "password123"}
    return valid_credentials.get(username) == password
