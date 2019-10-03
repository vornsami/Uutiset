from flask import render_template, request, redirect, url_for

from application import app, db
from application.tasks.models import News
from application.tasks.forms import NewsForm

from application.auth.models import User
from flask_login import login_required, current_user


@app.route("/news", methods=["GET"])
def news_index():
    return render_template("tasks/list.html", news = list(reversed((News.query.all()))))

@app.route("/news/new/")
@login_required
def news_form():
    return render_template("tasks/new.html", form = NewsForm())

@app.route("/news/", methods=["POST"])
@login_required
def news_create():
    n = News(request.form.get("title"),request.form.get("content"),current_user.username)

    db.session().add(n)
    db.session().commit()
  
    return redirect(url_for("news_index"))
    
@app.route("/news/<news_id>", methods=["GET", "POST"])
def news_read():
    print(request.form.get("name"))
  
    return "hello world!"
    