import os

TESTING = os.getenv('TESTING', False)
if TESTING:
    DATABASE = os.getenv('DATABASE_TEST')
    USER = os.getenv('USER_TEST')
    PASSWORD = os.getenv('PASSWORD_TEST')
    HOST = os.getenv('HOST_TEST')
    PORT = int(os.getenv('PORT_TEST'))
else:
    DATABASE = os.getenv('DATABASE')
    USER = os.getenv('USER')
    PASSWORD = os.getenv('PASSWORD')
    HOST = os.getenv('HOST')
    PORT = int(os.getenv('PORT'))