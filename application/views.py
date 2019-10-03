from flask import render_template
from application import app, db
from application.tasks.models import News

@app.route("/")
def aloitus():
    return render_template("index.html", news = list(reversed((News.query.all())))[:5])