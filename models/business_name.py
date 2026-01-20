from extensions import db

class BusinessName(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    registration_date = db.Column(db.DateTime, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def __repr__(self):
        return f"<BusinessName {self.name}>"


    first_name = db.Column(db.String(100))
    middle_name = db.Column(db.String(100))
    surname = db.Column(db.String(100))
    dob = db.Column(db.String(20))
    nationality = db.Column(db.String(50))
    state = db.Column(db.String(50))
    lga = db.Column(db.String(50))
    email = db.Column(db.String(120))
    phone = db.Column(db.String(20))
    residential_address = db.Column(db.Text)

    business_name = db.Column(db.String(150))
    business_address = db.Column(db.Text)
    description = db.Column(db.Text)

    nin = db.Column(db.String(11))
    status = db.Column(db.String(30), default="pending")

    photo = db.Column(db.String(255))
    nin_slip = db.Column(db.String(255))
    signature = db.Column(db.String(255))

