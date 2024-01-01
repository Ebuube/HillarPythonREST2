"""
Models to interact with
"""
from marshmallow import Schema, fields, pre_load
from marshmallow import validate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


orm = SQLAlchemy()
ma = Marshmallow()
