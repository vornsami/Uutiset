from flask import render_template, request, redirect, url_for

from application import app, db, login_manager, login_required
from application.tasks.models import News,Tag
from application.tasks.forms import NewsForm,TagForm
from flask_login import current_user

from application.auth.models import User

# Artikkeleihin liittyvät asiat

@app.route("/news", methods=["GET"])
def news_index():
    return render_template("tasks/list.html", news = list(reversed((News.query.all()))))

@app.route("/news/new/")
@login_required(role="ADMIN")
def news_form():
    return render_template("tasks/new.html", form = NewsForm())

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
    
    return render_template("tasks/read.html", 
                title = article[0], 
                content = article[1],
                tags = taglist
    )

#Artikkelin tagien ylläpito

@app.route("/news/<news_id>/tags", methods=["GET", "POST"])
@login_required(role="ADMIN")
def news_tag_management(news_id):
    
    return render_template("tasks/article_tags.html", 
                tags = Tag.query.all(),
                id = news_id
    )
 
@app.route("/news/<news_id>/tags/<tag_id>/", methods=["POST"])
@login_required(role="ADMIN")
def news_tag_add(news_id,tag_id):
    
    n = News.query.get(news_id)
    t = Tag.query.get(tag_id)
    n.tags.append(t)
    db.session().commit()
  
    return redirect(url_for("news_tag_management", news_id = news_id))


# Tageihin liittyvät asiat 

@app.route("/tags/new/")
@login_required(role="ADMIN")
def tag_form():
    return render_template("tasks/newtag.html", form = TagForm())

@app.route("/tags/", methods=["POST"])
@login_required(role="ADMIN")
def tag_create():
    n = Tag(request.form.get("name"))

    db.session().add(n)
    db.session().commit()
  
    return redirect(url_for("news_index"))
	
@app.route("/categories", methods=["GET"])
def categories():
    return render_template("tasks/categories.html", tags = Tag.query.all())

@app.route("/news/category/<tag_id>", methods=["GET","POST"])
def articles_with_tag(tag_id):

    a = Tag.find_articles_with_tag(tag_id)
	
    
    return render_template("tasks/list.html", news = list(reversed((a))))
	





    