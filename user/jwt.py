import os
import jwt
import datetime
from datetime import timedelta
from modelPj.settings import SECRET_KEY


# JWT_ALGORITHM = os.environ.get("JWT_ALGORITHM")
# SECRET_KEY = os.environ.get("SECRET_KEY")
JWT_ALGORITHM = 'HS256'
SECRET_KEY = SECRET_KEY

def encode_jwt(data):
    return jwt.encode(data, SECRET_KEY, algorithm=JWT_ALGORITHM).decode("utf-8")

def decode_jwt(access_token):
    return jwt.decode(
        access_token,
        SECRET_KEY,
        algorithms=[JWT_ALGORITHM],
        options={"verify_nickname": False},
    )
    
def generate_access_token(nickname):
    iat = datetime.now()
    exp = iat + timedelta(days=7)

    data = {
        "iat": iat.timestamp(),
        "exp": exp.timestamp(),
        "nickname": nickname,
    }

    return encode_jwt(data)