from functools import wraps
from .base import *

def check_connection(f):
    @wraps(f)
    def decorator(self: 'ETHBase', *args, **kwargs):
        if not self.isConnected:
            raise ConnectionError("Instance is not connected to ethereum node and mongo server")
        return f(self, *args, **kwargs)
    return decorator