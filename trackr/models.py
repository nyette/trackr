from trackr.db import db


class Item(db.Model):

    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    count = db.Column(db.Integer, nullable=False)
    in_trash = db.Column(db.Boolean, nullable=False, default=False)
    deletion_date = db.Column(db.DateTime)
    deletion_comment = db.Column(db.Text)

    def __init__(self, name, description, price, count):
        self.name = name
        self.description = description
        self.price = price
        self.count = count

    def __repr__(self):
        return f"<Item {self.name}>"
