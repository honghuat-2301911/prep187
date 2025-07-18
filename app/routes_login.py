from flask import Blueprint, render_template, request, redirect, url_for, flash

login_bp = Blueprint("login", __name__, url_prefix="/login")

@login_bp.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # Simple hardcoded login check
        if email == "admin" and password == "admin":
            return redirect(url_for("home.home"))  # route name is blueprint.function
        else:
            flash("Invalid credentials", "danger")

    return render_template("login.html")
