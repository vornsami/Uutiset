from flask import render_template, request, redirect, url_for

from application import app, db, login_manager, login_required
from application.articles.models import News,Tag
from application.articles.forms import NewsForm,TagForm
from flask_login import current_user

from application.auth.models import User



#Artikkelin tagien ylläpito

@app.route("/news/<news_id>/tags", methods=["GET", "POST"])
@login_required(role="ADMIN")
def news_tag_management(news_id):
    
    return render_template("articles/article_tags.html", 
                tags = Tag.query.all(),
                id = news_id
    )
 
@app.route("/news/<news_id>/tags/<tag_id>/", methods=["POST"])
@login_required(role="ADMIN")
def news_tag_add(news_id,tag_id):
    n = News.query.get(news_id)
    t = Tag.query.get(tag_id)
    if t not in n.tags:
        n.tags.append(t)
    else:
        n.tags.remove(t)
    db.session().commit()
  
    return redirect(url_for("news_tag_management", news_id = news_id))


# Tageihin liittyvät asiat 

@app.route("/tags/new/")
@login_required(role="ADMIN")
def tag_form():
    return render_template("articles/newtag.html", form = TagForm())

@app.route("/tags/", methods=["POST"])
@login_required(role="ADMIN")
def tag_create():
    n = Tag(request.form.get("name"))

    db.session().add(n)
    db.session().commit()
  
    return redirect(url_for("news_index"))
	
	
	




    