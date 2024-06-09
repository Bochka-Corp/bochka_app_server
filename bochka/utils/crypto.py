from passlib.handlers.pbkdf2 import pbkdf2_sha256


def set_password(password):
    return pbkdf2_sha256.hash(password)


def verify_password(password, password_hash):
    return pbkdf2_sha256.verify(password, password_hash)
