from flask import Flask, render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.auth.models import User
from application.auth.forms import NameForm, PasswordForm
from application.articles.models import Thread, Comment
      
@app.route("/newname", methods = ["GET", "POST"])
@login_required
def newname():
    if request.method == "GET":
        return render_template("auth/newname.html", form = NameForm())
        
    form = NameForm(request.form)
    
    if not form.validate():
        return render_template("auth/newname.html", form = form,
                               error = "Invalid name")
    
    user = User.query.filter_by(username=form.username.data).first()
    if user and not form.username.data == current_user.username:
        return render_template("auth/newname.html", form = form,
                               error = "Name already in use")
                               
    user = User.query.filter_by(name=form.username.data).first()
    if user:
        return render_template("auth/newname.html", form = form,
                               error = "Name already in use")
    
    current_user.name = form.username.data;
    db.session().commit()
    
    return redirect(url_for("userpage"))
    
@app.route("/newpassword", methods = ["GET", "POST"])
@login_required
def newpassword():
    if request.method == "GET":
        return render_template("auth/newpassword.html", form = PasswordForm())
        
    form = PasswordForm(request.form)
    
    if not form.validate():
        return render_template("auth/newpassword.html", form = form,
                               error = "Invalid password")
                               
    current_user.password = form.password.data;
    db.session().commit()
    
    return redirect(url_for("userpage"))
    
@app.route("/deleteUser", methods = ["POST"])
@login_required
def deleteUser():
    
    db.session().delete(current_user)
    db.session().commit()
    
    return redirect(url_for("aloitus"))
    

    

