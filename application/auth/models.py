from application import db
from sqlalchemy.sql import text
from sqlalchemy.orm import relationship

read_connect = db.Table('read', db.Model.metadata,
    db.Column('news_id', db.Integer, db.ForeignKey('news.id')),
    db.Column('account_id', db.Integer, db.ForeignKey('account.id'))
)


class User(db.Model):

    __tablename__ = "account"
  
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    acc_type = db.Column(db.String(144), nullable=False)
    
    read_articles = relationship("News",
                    secondary=read_connect,
                    backref="accounts_read")
    

    
    def __init__(self, name, username, password):
        print("account created")
        self.name = name
        self.username = username
        self.password = password
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
        
    def roles(self):
        return self.acc_type
        
    def is_admin(self):
        if self.acc_type == "ADMIN":
            return True        
        return False
    def get_read_articles(self):
        print(self.id)
        
        stmt = text("SELECT News.* FROM News,read,account WHERE account.id = :user_id AND read.news_id = News.id AND read.account_id = account.id;").params(user_id=self.id)
    
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append(row)
        
        return list(reversed(response))[:10]