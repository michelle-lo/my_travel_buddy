from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")
#"<h1>Test</h1>"

@views.route('/personal_info')
def home2():
    return render_template("get_personal_info.html")
#"<h1>Test</h1>"

@views.route('/dashboard')
def home3():
    return render_template("dashboard.html")
#"<h1>Test</h1>"