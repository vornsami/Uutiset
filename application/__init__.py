from flask import Flask, render_template

app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
app.config["SQLALCHEMY_ECHO"] = True


import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///newsdb.db"    
    app.config["SQLALCHEMY_ECHO"] = True


db = SQLAlchemy(app)

from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "aloitus"
login_manager.login_message = "Unauthorized."

from functools import wraps
from flask_login import current_user
def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user:
                return login_manager.unauthorized()

            if not current_user.is_authenticated:
                return login_manager.unauthorized()
            
            unauthorized = False

            if role != "ANY":
                unauthorized = True
                
                if current_user.roles() == role:
                    unauthorized = False
                    

            if unauthorized:
                return login_manager.unauthorized()
            
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper
	
	
from application import views

from application.articles import models
from application.articles import views

from application.management import views

from application.auth import models
from application.auth import views

from application.auth.models import User
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

try: 
    db.create_all()
except:
    pass
	
#Luodaan admin-käyttäjä, mikäli sellaista ei vielä ole	
admin = User.query.filter_by(id=1,username="admin").first()
if not admin:
    u = User("admin","admin","admin")
    u.acc_type = "ADMIN"
    u.id = 1
    db.session().add(u)
    db.session().commit()
