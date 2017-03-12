class DevelopmentConfig(object):
    DATABASE_URI = "postgresql://ubuntu:thinkful@localhost:5432/posts"
    DEBUG = True

class TestingConfig(object):
    DATABASE_URI = "postgresql://ubuntu:thinkful@localhost:5432/posts-test"
    DEBUG = True
    
class TravisConfig(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://ubuntu@localhost:5432/posts-test"
    DEBUG = False
    SECRET_KEY = "Not secret"
