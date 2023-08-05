# Flask Application Stuff
from flask import Flask, render_template, request, session, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text, ForeignKey
from passlib.hash import sha256_crypt
from datetime import datetime

from helpers import login_required, is_even

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "cs50"
app.config['SESSION_COOKIE_EXPIRES'] = None  # Expire when the browser is closed
db = SQLAlchemy(app)
app.app_context().push() # Needed or else breaks

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    username = db.Column(db.String(100))
    
class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    serviceType = db.Column(db.String(100))
    servicePrice = db.Column(db.String(100))
    serviceDescription = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    
db.create_all()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/order", methods = ["GET", "POST"])
def order():
    if request.method == "POST":
        service_name = request.form.get("service_name")
        price = request.form.get("service_price")
        description = request.form.get("service_description")
        new_order = Orders(serviceType=service_name, servicePrice=price, serviceDescription=description, user_id=session["user_id"])
        db.session.add(new_order)
        db.session.commit()
        return redirect(url_for('history'))
    else:
        return render_template("order.html")

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        invalid_login = False
        email = request.form.get("email")
        password = request.form.get("password")
        query = text("SELECT password FROM user WHERE email=:email")
        result = db.session.execute(query, {"email": email})
        server_password = result.scalar()
        
        
        if server_password is not None and sha256_crypt.verify(password, server_password): #Successful Login
            query = text("SELECT id FROM user WHERE password=:password")
            result = db.session.execute(query, {"password": server_password})
            session["user_id"] = result.scalar() # Gets user_id into the session.
            query = text("SELECT username FROM user WHERE password=:password")
            result = db.session.execute(query, {"password": server_password})
            session["username"] = result.scalar() # Gets Username into the session.
            return redirect(url_for("order"))
        invalid_login=True
        return render_template("login.html", invalid_login=invalid_login)
    elif request.method == "GET":
        return render_template("login.html") 


@app.route("/register", methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get("email")
        username = request.form.get("username")
        password = sha256_crypt.encrypt(request.form.get("password"))
        confirm_password = request.form.get("confirm_password")
        
        #check if email is taken
        query = text("SELECT * FROM user WHERE email=:email")
        result = db.session.execute(query, {"email": email})
        print(result)
        if not result:
            email_taken = True
            return render_template("register.html", email_taken=email_taken)
            
        #check if confirm/password match:
        if not sha256_crypt.verify(confirm_password, password):
            return "Confirmation and Password did not match!"

        new_user = User(email=email, password=password, username=username)
        db.session.add(new_user)
        db.session.commit()
        
        return render_template("login.html")
    
    elif request.method == "GET":
        return render_template("register.html")

@app.route("/history", methods = ['GET'])
def history():
    if "username" in session:
        user_id = session['user_id'] # Integer
        query = text("SELECT id, serviceType, servicePrice, serviceDescription FROM orders WHERE user_id=:user_id")
        result = db.session.execute(query, {'user_id': user_id})
        return render_template("history.html", orderInfo=result, is_even=is_even)
    else:
        return render_template("index.html") # User wasn't signed in
    
@app.route("/logout", methods = ['GET'])
def logout():
    session.pop("username", None)
    session.pop("user_id", None)
    logout_worked = True
    return render_template("login.html", logout=logout_worked)
    
if __name__ == "__main__":
    app.run(debug=True)