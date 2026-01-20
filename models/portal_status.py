from extensions import db

class PortalStatus(db.Model):
    __tablename__ = "portal_status"

    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(50), unique=True, nullable=False)
    status = db.Column(db.String(20), nullable=False, default="inactive")
