from .app import db


class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)

    def __init__(self,name,lat,lon):
        self.name = name
        self.lat = lat
        self.lon = lon

    def __repr__(self):
        return '<Pet %r>' % (self.name)
