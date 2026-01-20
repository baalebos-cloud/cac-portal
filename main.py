from flask import Flask
from config import Config
from extensions import db, mail, jwt, login_manager
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    jwt.init_app(app)
    login_manager.init_app(app)

    # Login manager config
    login_manager.login_view = "admin.login"

    # ---------------- REGISTER BLUEPRINTS ---------------- #
    from routes.business_name import business_name_bp
    from routes.company import company_bp
    from routes.ngo import ngo_bp
    from routes.admin import admin_bp

    app.register_blueprint(business_name_bp, url_prefix="/business-name")
    app.register_blueprint(company_bp, url_prefix="/company")
    app.register_blueprint(ngo_bp, url_prefix="/ngo")
    app.register_blueprint(admin_bp, url_prefix="/admin")

    return app


# App entry point
app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

