from app import create_app
from extensions import db
from models import PortalStatus

app = create_app()

with app.app_context():
    portal = PortalStatus.query.filter_by(key="main_portal").first()
    if not portal:
        portal = PortalStatus(key="main_portal", status="inactive")
        db.session.add(portal)
        db.session.commit()
        print("PortalStatus initialized.")
    else:
        print("PortalStatus already exists:", portal.status)
