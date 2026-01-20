from flask import Flask
from models import PortalStatus

@app.route("/")
def home():
    portal = PortalStatus.query.filter_by(key="main_portal").first()
    if portal and portal.status == "active":
        return "<h1>Oluwadare T J CAC Portal is Live!</h1>"
    return "<h1>Portal is Inactive</h1>"
