from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login_page.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        #implement later
        # if len(email) < 4:
        #     flash("Email invalid", category="error")
        # elif len(firstName) < 2:
        #     flash("First name invalid", category="error")
        # elif len(lastName) < 2:
        #     flash("Last name invalid", category="error")
        # elif password1 != password2:
        #     flash("Passwords must match", category="error")
        # elif len(password1) < 7:
        #     flash("Password invalid", category="error")
        # else:
        #     flash("Success", category="success")
        
            #something happens
    
    return render_template("sign_up.html", boolean=True)

