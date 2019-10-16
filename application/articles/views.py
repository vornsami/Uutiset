from flask import render_template, request, redirect, url_for

from application import app, db, login_manager, login_required
from application.articles.models import News,Tag
from application.articles.forms import NewsForm,TagForm
from flask_login import current_user

from application.auth.models import User

# Artikkeleihin liittyvät asiat

@app.route("/news", methods=["GET"])
def news_index():
    return render_template("articles/list.html", news = list(reversed((News.query.all()))))

@app.route("/news/new/")
@login_required(role="ADMIN")
def news_form():
    return render_template("articles/new.html", form = NewsForm())

@app.route("/news/", methods=["POST"])
@login_required(role="ADMIN")
def news_create():
    n = News(request.form.get("title"),request.form.get("content"),current_user.username)

    db.session().add(n)
    db.session().commit()
  
    return redirect(url_for("news_index"))
    
@app.route("/news/<news_id>/", methods=["GET", "POST"])
def news_read(news_id):
    
    article = News.find_article(news_id)
    taglist = News.find_tags(news_id)
	
    if current_user.is_authenticated:
        
        n = News.query.get(news_id)
        u = User.query.get(current_user.id)
        u.read_articles.append(n)
        db.session().commit()		
    
    return render_template("articles/read.html", 
                title = article[0], 
                content = article[1],
                tags = taglist
    )
	
@app.route("/categories", methods=["GET"])
def categories():
    return render_template("articles/categories.html", tags = Tag.query.all())

@app.route("/news/category/<tag_id>", methods=["GET","POST"])
def articles_with_tag(tag_id):

    a = Tag.find_articles_with_tag(tag_id)
	
    
    return render_template("articles/list.html", news = list(reversed((a))))
	





    