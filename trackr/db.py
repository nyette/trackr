from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Item(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), nullable = False)
    description = db.Column(db.Text, nullable = False)
    price = db.Column(db.Float, nullable = False)
    count = db.Column(db.Integer, nullable = False)
    in_trash = db.Column(db.Boolean, nullable = False, default = False)
    
    def __repr__(self):
        return f"<Item {self.id} {self.name}>"
    