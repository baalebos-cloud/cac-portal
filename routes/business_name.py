from flask import Blueprint, request, redirect, render_template, url_for, flash
from extensions import db
from models.business_name import BusinessName

business_name_bp = Blueprint("business_name", __name__, url_prefix="/business")

# ---------------- INDEX PAGE ---------------- #
@business_name_bp.route("/index", endpoint="index")
def index():
    # Fetch all existing business records
    businesses = BusinessName.query.all()
    return render_template("business/index.html", businesses=businesses, title="Business Index")


# ---------------- SUBMIT BUSINESS NAME ---------------- #
@business_name_bp.route("/submit", methods=["POST"], endpoint="submit_business_name")
def submit_business_name():
    try:
        data = request.form

        # Create a new BusinessName record
        record = BusinessName(
            first_name=data.get("first_name"),
            middle_name=data.get("middle_name"),
            surname=data.get("surname"),
            date_of_birth=data.get("date_of_birth"),
            nationality=data.get("nationality"),
            state_of_origin=data.get("state_of_origin"),
            lga=data.get("lga"),
            email=data.get("email"),
            residential_address=data.get("residential_address"),
            house_number=data.get("house_number"),
            business_address=data.get("business_address"),
            business_description=data.get("business_description"),
            proposed_business_name=data.get("proposed_business_name"),
            nin_number=data.get("nin_number"),
            phone_number=data.get("phone_number"),
        )

        # Save to database
        db.session.add(record)
        db.session.commit()

        # Flash a success message and redirect back to index
        flash("Business Name submitted successfully!", "success")
        return redirect(url_for("business_name.index"))

    except Exception as e:
        db.session.rollback()
        flash(f"Error submitting business: {str(e)}", "danger")
        return redirect(url_for("business_name.index"))
