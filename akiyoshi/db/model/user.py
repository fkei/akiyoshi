import sqlalchemy
from sqlalchemy.orm import mapper, clear_mappers

from __init__ import Model

def get_user(metadata, now):
    return sqlalchemy.Table("user", metadata,
                            sqlalchemy.Column('id', sqlalchemy.Integer,
                                              primary_key=True,
                                              autoincrement=True,
                                              ),
                            sqlalchemy.Column('email', sqlalchemy.String(256),
                                              unique=True,
                                              nullable=False,
                                              ),
                            sqlalchemy.Column('password', sqlalchemy.String(40),
                                              nullable=False,
                                              ),
                            sqlalchemy.Column('salt', sqlalchemy.Unicode(16),
                                              nullable=False,
                                              ),
                            sqlalchemy.Column('nickname', sqlalchemy.Unicode(16),
                                              nullable=False,
                                              ),
                            sqlalchemy.Column('created', sqlalchemy.DateTime,
                                              default=now,
                                              ),
                            sqlalchemy.Column('modified', sqlalchemy.DateTime,
                                              default=now,
                                              onupdate=now,
                                              ),
                            )

class User(Model):
    def __init__(self, email, password, salt, nickname):
        self.email = email
        self.password = password
        self.salt = salt
        self.nickname = nickname

    def json(self):
        return {
            "id": self.id,
            "email": self.email,
            "nickname": self.nickname,
            "created": self.created,
            "modified": self.modified
        }

    def __repr__(self):
        return "User<'%s>" % (self.email)

def reload_mapper(metadata, now):

    t_user = get_user(metadata,now)
    mapper(User, t_user)

