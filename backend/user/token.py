import datetime

from jwt import decode
from jwt import encode


def GetToken(email, userid):
    time = datetime.datetime.now()
    return encode({'email': email, 'logintime': str(time), 'id': userid, 'type': 0
                   }, 'secret_key', algorithm='HS256')


def Check(token):
    try:
        s = decode(token, 'secret_key', algorithms='HS256')
    except:
        return -1, -1
    return s.get('id', -1), s.get('type', -1)