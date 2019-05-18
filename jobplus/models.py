from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, current_user
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Base(db.Model):   
    __abstract__ = True
    create_at = db.Column(db.DateTime, default=datetime.now)
    update_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)


# 用户表映射类，个人用户和企业用户共用此表
class User(Base, UserMixin):
    ROLE_USER = 11
    ROLE_COMPANY = 22
    ROLE_ADMIN = 33
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True, nullable=False)
    email = db.Column(db.String(128), unique=True, index=True, nullable=False)
    _password = db.Column('password', db.String(256), nullable=False)
    role = db.Column(db.SmallInteger, default=ROLE_USER)  # 角色
    is_disable = db.Column(db.Boolean, default=False)     # 封用户时用

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, p):
        self._password = generate_password_hash(p)

    def check_password(self, p):
        return check_password_hash(self._password, p)

    @property   # 判断用户是不是管理员
    def is_admin(self):
        return self.role == self.ROLE_ADMIN

    @property   # 判断用户是不是个人用户
    def is_user(self):
        return self.role == self.ROLE_USER

    @property   # 判断用户是不是企业用户
    def is_company(self):
        return self.role == self.ROLE_COMPANY

class Company(Base):

    __tablename__ = 'company'
    
    id = db.Column(db.Integer,db.ForeignKey('user.id'),primary_key=True)
    name = db.Column(db.String(256))
    logo = db.Column(db.String(32))
    web = db.Column(db.String(64))
    description = db.Column(db.String(512))
    user = db.relationship('User',uselist=False,backref='company')


class Resume(Base):
    __tablename__ = 'resume'

    id = db.Column(db.Integer,db.ForeignKey('user.id'),primary_key=True)
    name = db.Column(db.String(64))
    
    work_experience = db.Column(db.SmallInteger)
    edu_experience = db.Column(db.SmallInteger)
    user = db.relationship('User',uselist=False,backref='resume')



