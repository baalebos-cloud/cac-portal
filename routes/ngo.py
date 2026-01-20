from flask import Blueprint, render_template, redirect, url_for, flash
from extensions import db
from models.ngo import NGO
from models.payment import Payment
from forms import NGOForm   # ✅ import the new form

ngo_bp = Blueprint("ngo", __name__, template_folder="../templates")

@ngo_bp.route("/", methods=["GET", "POST"])
def register_ngo():
    form = NGOForm()
    if form.validate_on_submit():   # ✅ use Flask-WTF validation
        try:
            # Create NGO record from form data
            ngo = NGO(
                proposed_name_1=form.name.data,        # adapt field names
                mission=form.trustees.data,            # trustees text area
                # add other fields if you extend NGOForm later
            )

            db.session.add(ngo)
            db.session.commit()

            # Create Payment record
            payment = Payment(
                service="NGO Registration",
                amount=ngo.amount,     # assumes NGO model has an amount field
                status="Pending",
                reference=f"NGO-{ngo.id}"
            )

            db.session.add(payment)
            db.session.commit()

            flash("NGO registration submitted successfully", "success")
            return redirect(url_for("ngo.register_ngo"))

        except Exception as e:
            db.session.rollback()
            flash(f"Error: {str(e)}", "danger")

    # Render template with form
    return render_template("ngo_register.html", form=form)
