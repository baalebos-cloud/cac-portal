from flask import Flask
from config import Config
from extensions import db, mail, jwt, login_manager, migrate
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    jwt.init_app(app)
    login_manager.init_app(app)

# ---------------- ROOT ROUTE ---------------- #
    @app.route("/")
    def home():
        return "<h1>Oluwadare T J Merchandise Co limited CAC Portal is Live!</h1>"

# ---------------- REGISTER BLUEPRINTS ---------------- #
    from routes.business_name import business_name_bp
    from routes.company import company_bp
    from routes.ngo import ngo_bp
    from routes.admin import admin_bp

    app.register_blueprint(business_name_bp, url_prefix="/business")
    app.register_blueprint(company_bp, url_prefix="/company")
    app.register_blueprint(ngo_bp, url_prefix="/ngo")
    app.register_blueprint(admin_bp, url_prefix="/admin")

    # ---------------- HEALTH CHECK ROUTE ---------------- #
    @app.route("/health")
    def health():
        return {"status": "OK", "message": "CAC portal is live"}

    return app

# Run the app directly (optional, for local dev)
if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8000, debug=True)
