from application import db

tag_connect = db.Table('connect', db.Model.metadata,
    db.Column('news_id', db.Integer, db.ForeignKey('news.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
)


class News(db.Model):
    __tablename__ = 'news'
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    title = db.Column(db.String(144), nullable=False)
    content = db.Column(db.String(8000), nullable=False)
    
    writer = db.Column(db.String(144), nullable=False)

    def __init__(self, title, content, writer):
        self.title = title
        self.content = content
        self.writer = writer
        
class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer,primary_key=True)
    
    name=db.Column(db.String(144), nullable=False)
    
    def __init__(self, name):
        self.name = name
        
        