from .user import __table__ as USER
from .file import __table__ as FILE

def init_database():
    USER.init()
    FILE.init()