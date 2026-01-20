from flask import Blueprint, render_template, request, redirect, url_for, flash
from extensions import db
from models.company import Company
from models.payment import Payment

# Define the blueprint
company_bp = Blueprint("company", __name__, template_folder="../templates")

@company_bp.route("/", methods=["GET", "POST"])
def register_company():
    if request.method == "POST":
        try:
            # Create a new Company object from form data
            company = Company(
                proposed_name_1=request.form.get("proposed_name_1"),
                proposed_name_2=request.form.get("proposed_name_2"),
                business_nature=request.form.get("business_nature"),
                state=request.form.get("state"),
                lga=request.form.get("lga"),
                city=request.form.get("city"),
                street=request.form.get("street"),
                phone=request.form.get("phone"),
                email=request.form.get("email")
            )

            db.session.add(company)
            db.session.commit()

            # ⚠️ Ensure your Company model defines `amount`
            # If not, you’ll need to calculate or set it before using
            payment = Payment(
                service="Company Registration",
                amount=getattr(company, "amount", 0),  # safer fallback
                status="Pending",
                reference=f"COMP-{company.id}"
            )

            db.session.add(payment)
            db.session.commit()

            flash("Company registration submitted successfully", "success")
            return redirect(url_for("company.register_company"))

        except Exception as e:
            db.session.rollback()
            flash(f"Error: {str(e)}", "danger")

    # Render the company registration template
    return render_template("company.html")
