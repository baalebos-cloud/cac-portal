from extensions import db
from datetime import datetime
from models import PortalStatus
# -------------------------------------------
# SQLAlchemy Models for CAC Portal
# -------------------------------------------

class BusinessName(db.Model):
    __tablename__ = "business_names"  # explicit table name
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    nin = db.Column(db.String(11), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    status = db.Column(db.String(30), default="pending")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Optional: Track portal status
class PortalStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(50), unique=True, nullable=False)
    status = db.Column(db.String(20), nullable=False, default="inactive")
