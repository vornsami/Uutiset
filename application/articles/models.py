from application import db
from sqlalchemy.sql import text
from sqlalchemy.orm import relationship

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
    
    tags = relationship("Tag",
                    secondary=tag_connect,
                    back_populates="articles")

    def __init__(self, title, content, writer):
        self.title = title
        self.content = content
        self.writer = writer
        
        
    @staticmethod
    def find_article(x):
        
        stmt = text("SELECT * FROM News WHERE id = :x ;").params(x=x)
        
        res = db.engine.execute(stmt).fetchall()
        response = []
    
        
        response.append(res[0]['title'])
        response.append(res[0]['content'])
        
        print(response)
        return response
        
    @staticmethod
    def find_tags(x):
    
        stmt = text("SELECT Tag.name FROM News,Connect,Tag WHERE news.id = :x AND Connect.news_id = News.id AND Connect.tag_id = Tag.id;").params(x=x)
    
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({row['name']})
    
        return response
    
        
class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer,primary_key=True)
    
    name=db.Column(db.String(144), nullable=False)
    
    articles = relationship("News",
        secondary=tag_connect,
        back_populates="tags")
    
    def __init__(self, name):
        self.name = name

    @staticmethod
    def find_articles_with_tag(x):
    
        stmt = text("SELECT News.* FROM News,Connect,Tag WHERE tag.id = " + x + " AND Connect.news_id = News.id AND Connect.tag_id = Tag.id;")
    
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "title":row[3]})
    
        return response
        
        