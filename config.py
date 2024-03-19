import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://traffic:traffic@localhost/traffic') 
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # SQLAlchemy의 객체 변경 추적 기능을 비활성화하여 성능을 최적화하는 설정
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False  # autocommit 비활성화
    SECRET_KEY = 'b3623a3c8a4943c6dd94a6bff0099d69' #세션관리위해 추가
    