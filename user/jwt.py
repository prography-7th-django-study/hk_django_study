import jwt
from datetime import datetime, timedelta
from modelPj.settings import SECRET_KEY

JWT_ALGORITHM = 'HS256'

def encode_jwt(data):
    return jwt.encode(data, SECRET_KEY, algorithm=JWT_ALGORITHM)

def decode_jwt(access_token):
    access_token = str.replace(str(access_token), 'Bearer ', '')
    access_token = access_token[1:-1]
    return jwt.decode(
        access_token,
        SECRET_KEY,
        algorithms=JWT_ALGORITHM,
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