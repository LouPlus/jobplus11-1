from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField, BooleanField,
        ValidationError, IntegerField)
from wtforms.validators import Length,Email,EqualTo,DataRequired
from jobplus.models import db,User,Resume,Company
from flask_login import current_user

class RegisterForm(FlaskForm):

        name = StringField('用户名',validators=[DataRequired(),Length(3,24)])

        email = StringField('邮箱',validators=[DataRequired(),Email()])
        password = PasswordField('密码',validators=[DataRequired(),Length(6,24)])
        repeat_password = PasswordField('重复密码',validators=[DataRequired(),EqualTo('password')])
        submit = SubmitField('提交')

        def create_user(self):
                user = User()
                user.name = self.name.data
                user.email = self.email.data
                user.password = self.password.data
                db.session.add(user)
                db.session.commit()
                return user

        
        def create_company_user(self):
                user = User()
                user.name = self.name.data
                user.email = self.email.data
                user.password = self.password.data
                user.role = 22
                db.session.add(user)
                db.session.commit()
                return user
        
        def validate_username(self,field):

                if User.query.filter_by(name=field.data).first():

                        raise ValidationError('用户名已存在')
        
        def validate_email(self,field):
                if User.query.filter_by(email=field.data).first():
                        raise ValidationError('邮箱已存在')

class LoginForm(FlaskForm):
        
        email = StringField('邮箱',validators=[DataRequired(),Email()])
        password = PasswordField('密码',validators=[DataRequired(),Length(6,24)])
        remember_me = BooleanField('记住我')
        submit = SubmitField('提交')
        
        def validate_email(self,field):
                if not User.query.filter_by(email=field.data).first():
                        raise ValidationError('邮箱未注册')

        def validate_password(self,field):
                user = User.query.filter_by(email=self.email.data).first()
                if user and not user.check_password(field.data):
                        raise ValidationError('密码错误')

class UserProfileForm(FlaskForm):
        
        name = StringField('简历名称')
        work_experience= IntegerField('工作经验')
        edu_experience = IntegerField('教育经验')
        submit = SubmitField('保存')

        def create_resume(self):
            resume = Resume()
            resume.id = current_user.id
            self.populate_obj(resume)
            #resume.name = self.name.data
            #resume.work_experience = self.work_experience.data
            #resume.edu_experience = self.edu_experience.data
            db.session.add(resume)
            db.session.commit()
            return resume
