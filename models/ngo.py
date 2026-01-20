from extensions import db

class NGO(db.Model):
    __tablename__ = "ngos"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)

    # Relationships
    directors = db.relationship("NGODirector", back_populates="ngo", cascade="all, delete-orphan")
    trustees = db.relationship("Trustee", back_populates="ngo", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<NGO {self.name}>"

class NGODirector(db.Model):
    __tablename__ = "ngo_directors"   # ✅ Unique table name

    id = db.Column(db.Integer, primary_key=True)
    ngo_id = db.Column(db.Integer, db.ForeignKey("ngos.id"), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20))
    nin = db.Column(db.String(11))

    ngo = db.relationship("NGO", back_populates="directors")

    def __repr__(self):
        return f"<NGODirector {self.surname} {self.first_name}>"

class Trustee(db.Model):
    __tablename__ = "trustees"

    id = db.Column(db.Integer, primary_key=True)
    ngo_id = db.Column(db.Integer, db.ForeignKey("ngos.id"), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50))
    nin = db.Column(db.String(11))

    ngo = db.relationship("NGO", back_populates="trustees")

    def __repr__(self):
        return f"<Trustee {self.surname} {self.first_name}>"
