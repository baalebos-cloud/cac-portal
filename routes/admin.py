from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from extensions import db, login_manager
from models import PortalStatus
from models.user import User
from models.business_name import BusinessName
from models.company import Company
from models.ngo import NGO
from models.payment import Payment
from whatsapp import send_whatsapp_alert  # your WhatsApp function

admin_bp = Blueprint("admin", __name__, template_folder="../templates")
admin_bp = Blueprint("admin", __name__, url_prefix="/admin")
admin_bp = Blueprint('admin', __name__)

# ---------------- LOGIN MANAGER ---------------- #
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# ---------------- ADMIN LOGIN ---------------- #
@admin_bp.route("/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(
            email=email,
            is_admin=True
        ).first()

        if user and user.check_password(password):
            login_user(user)
            flash("Login successful", "success")
            return redirect(url_for("admin.dashboard"))
        else:
            flash("Invalid credentials", "danger")

    return render_template("admin_login.html")

# ---------------PORTAL STATUS-------------- #
@admin_bp.route("/portal/status/update", methods=["POST"])
@login_required
def update_portal_status():
    # Get the new status from form: "active" or "inactive"
    new_status = request.form.get("status")
    portal = PortalStatus.query.filter_by(key="main_portal").first()
    if not portal:
        portal = PortalStatus(key="main_portal", status=new_status)
        db.session.add(portal)
    else:
        portal.status = new_status

    db.session.commit()
    flash(f"Portal status updated to {new_status}", "success")
    return redirect(url_for("admin.admin_dashboard"))

# ---------------- ADMIN DASHBOARD ---------------- #
@admin_bp.route("/dashboard")
@login_required
def dashboard():
    business_names = BusinessName.query.all()
    companies = Company.query.all()
    ngos = NGO.query.all()
    payments = Payment.query.all()

    return render_template(
        "admin_dashboard.html",
        business_names=business_names,
        companies=companies,
        ngos=ngos,
        payments=payments
    )


# ---------------- UPDATE PAYMENT STATUS ---------------- #
@admin_bp.route("/payment/<int:payment_id>/update", methods=["POST"])
@login_required
def update_payment_status(payment_id):
    """Update payment status and notify user via WhatsApp if status changes."""
    # Fetch the payment record
    payment = Payment.query.get_or_404(payment_id)

    # Get the new status from the form
    new_status = request.form.get("status")

    if payment.status != new_status:
        # Update payment
        payment.status = new_status
        db.session.commit()

        # Send WhatsApp notification if user exists
        if hasattr(payment, "user") and payment.user and payment.user.phone_number:
            message = f"Hello {payment.user.first_name}, your payment status has been updated to '{new_status}'."
            send_whatsapp_alert(payment.user.phone_number, message)

        flash("Payment status updated and user notified via WhatsApp.", "success")
    else:
        flash("No changes made to payment status.", "info")

    return redirect(url_for("admin.admin_dashboard"))

@admin_bp.route('/admin/update_payment_ajax/<int:payment_id>', methods=['POST'])
def update_payment_ajax(payment_id):
    data = request.get_json()
    new_status = data.get('status')

    if not new_status:
        return jsonify({'success': False, 'message': 'Invalid status'}), 400

    payment = Payment.query.get(payment_id)
    if not payment:
        return jsonify({'success': False, 'message': 'Payment not found'}), 404

    payment.status = new_status
    db.session.commit()

    return jsonify({'success': True, 'message': 'Payment status updated successfully'})

    # Trigger WhatsApp notification
    try:
        send_whatsapp_alert(
            phone_number=payment.user.phone_number,
            user_name=payment.user.first_name,
            payment_id=payment.id,
            amount=payment.amount,
            status=new_status
        )
    except Exception as e:
        print("WhatsApp Error:", e)

    return jsonify({'success': True, 'message': 'Status updated'})

# ---------------- LOGOUT ---------------- #
@admin_bp.route("/logout")
@login_required
def admin_logout():
    logout_user()
    flash("Logged out successfully", "info")
    return redirect(url_for("admin.admin_login"))
