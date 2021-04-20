from sqlalchemy.orm import backref
from . import db
from app.models.music_model import MusicModel

class BandModel(db.Model):
    __tablename__ = "bands"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    music_list = db.relationship('MusicModel', backref='band')
    