# models.py


import datetime
from app import db


class Post(db.Model):

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    price = db.Column(db.String, nullable=False)
    

    def __init__(self, text, category, price):
        self.text = text
        self.category = category
        self.price = price
