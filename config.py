class DevConfig:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost:3306/test?charset=UTF8MB4"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
