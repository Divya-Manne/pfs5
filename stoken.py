# from key import secret_key,salt
# from itsdangerous import URLSafeTimedSerializer
# def token(data):
#     serializer=URLSafeTimedSerializer(secret_key)
#     return serializer.dumps(data,salt=salt)
# def dtoken(data):
#     serializer=URLSafeTimedSerializer(secret_key)
#     return serializer.loads(data,salt=salt)
from itsdangerous import URLSafeTimedSerializer
from key import salt,secret_key
def token(data):
    serializer=URLSafeTimedSerializer(secret_key)
    return serializer.dumps(data,salt=salt)
def dtoken(data):
    serializer=URLSafeTimedSerializer(secret_key)
    return serializer.loads(data,salt=salt)