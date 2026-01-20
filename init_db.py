from app import create_app  # only import the factory
from extensions import db  # import db from extensions
from models import PortalStatus, Company, Director, Shareholder  # import your model

app = create_app()  # Initialize your Flask app

# Run inside the app context
with app.app_context():
    db.drop_all()
    db.create_all()

    # Insert default portal_status if not exists
    if not PortalStatus.query.filter_by(key="main_portal").first():
        status = PortalStatus(key="main_portal", status="active")
        db.session.add(status)
        db.session.commit()

    print("Database initialized successfully!")
