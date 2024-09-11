from decouple import config #will allow us to use environment variables

class Config: 
    SECRET_KEY = config('SECRET_KEY') #Configuring the secret key from .env
    SQLALCHEMY_DATABASE_URI = f"mysql://{config('MYSQL_USER')}:{config('MYSQL_PASSWORD')}@{config('MYSQL_HOST')}/{config('MYSQL_DB')}" #Cnnecting with the db using varaibles from.env
    SQLALCHEMY_TRACK_MODIFICATIONS = False #Disable tracking of changes
