from application import db

class Plants(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    com_name = db.Column(db.String(30))
    sci_name = db.Column(db.String(30), nullable=False)
    pla_gar = db.relationship('Pla_Gar', backref='Plants')

class Gardens(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(50), nullable=False)
    pla_gar = db.relationship('Pla_Gar', backref='Gardens')

class Pla_Gar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plant_id = db.Column(db.Integer, db.ForeignKey('plants.id'), nullable=False)
    garden_id = db.Column(db.Integer, db.ForeignKey('gardens.id'), nullable=False)