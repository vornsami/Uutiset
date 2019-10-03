from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

class NewsForm(FlaskForm):
    title = StringField("News title", [validators.Length(min=2)])
    content = TextAreaField("News content", [validators.Length(min=2)])
 
    class Meta:
        csrf = False