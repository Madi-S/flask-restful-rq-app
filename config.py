from os import environ


class Configuration:
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'super_secret_hasehd_encrypted_key_to_protect_my_sophisticated_web_application_from_various_hackers_on_a_daily_basis'
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/retful.db'                  # 'mysql+mysqlconnector://root:1234@localhost/restful'