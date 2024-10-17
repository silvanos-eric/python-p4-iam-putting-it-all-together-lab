from config import bcrypt, db
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin


class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Integer, nullable=False, unique=True)
    _password_hash = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String)

    @hybrid_property
    def password_hash(self):
        raise AttributeError('Private field, _password_hash is not accessible')

    @password_hash.setter
    def password_hash(self, password):
        self._password_hash = bcrypt.generate_password_hash(password).decode(
            'utf-8')


class Recipe(SerializerMixin):
    __tablename__ = 'recipes'

    pass
