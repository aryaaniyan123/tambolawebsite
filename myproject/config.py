import os

class config(object):
   DEBUG = False
   TESTING = False
['SQLALCHEMY_TRACK_MODIFICATION'] = False
['SECRET_KEY'] = '!9m@S-dThyIlW[pHQbN^'
['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/auth'
['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
['JWT_SECRET_KEY'] = 'Dude!WhyShouldYouEncryptIt'
['JWT_BLACKLIST_ENABLED'] = True
['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']


class ProductionConfig(config):
    pass

class DevelopmentConfig(config):
    DEBUG = True

['SECRET_KEY'] = '!9m@S-dThyIlW[pHQbN^'
['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/auth'
['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
['JWT_SECRET_KEY'] = 'Dude!WhyShouldYouEncryptIt'
['JWT_BLACKLIST_ENABLED'] = True
['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']


class TestingConfig(config):
    TESTING = True

