"""
Configuration for database
"""
import os


basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = True    # Will change it to False later
SQLALCEMY_TRACK_MODIFICATIONS = True
# Replace your_user_name with the user name you configured for the database
# Replace your_password with the password you specified for the database user
SQLALCHEMY_DATABASE_URI = "postgresql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}".format(DB_USER="root", DB_PASS="root_at_psql", DB_ADDR="127.0.0.1", DB_NAME="flask_notifications")
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
