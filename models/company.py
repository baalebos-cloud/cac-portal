from extensions import db

class Company(db.Model):
    __tablename__ = "company"
    id = db.Column(db.Integer, primary_key=True)
    proposed_name1 = db.Column(db.String(150))
    proposed_name2 = db.Column(db.String(150))
    business_address = db.Column(db.Text)
    email = db.Column(db.String(120))
    phone = db.Column(db.String(20))
    share_capital = db.Column(db.String(50))
    status = db.Column(db.String(30), default="pending")

class Director(db.Model):
    __tablename__ = "directors"
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey("company.id"))
    surname = db.Column(db.String(100))
    first_name = db.Column(db.String(100))
    email = db.Column(db.String(120))
    phone = db.Column(db.String(20))
    nin = db.Column(db.String(11))

class Shareholder(db.Model):
    __tablename__ = "shareholders"
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey("company.id"))
    surname = db.Column(db.String(100))
    first_name = db.Column(db.String(100))
    shares = db.Column(db.Integer)
