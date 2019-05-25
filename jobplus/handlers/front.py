from flask import Blueprint,render_template
from flask import flash,redirect,url_for
from flask_login import login_user,logout_user,login_required
from jobplus.forms import LoginForm,RegisterForm

from jobplus.models import User,db


front = Blueprint('front',__name__)

@front.route('/')
def index():
        return render_template('index.html')

@front.route('/login',methods=['GET','POST'])
def login():
        form = LoginForm()
        if form.validate_on_submit():
                user = User.query.filter_by(email=form.email.data).first()
                login_user(user,form.remember_me.data)
                return redirect(url_for('.index'))
        return render_template('login.html',form=form)

@front.route('/company_register',methods=['GET','POST'])
def company_register():
        form = RegisterForm()
        if form.validate_on_submit():
                user=form.create_user()
                user.role = User.ROLE_COMPANY
                db.session.add(user)
                db.session.commit()
                flash('注册成功，请登录！','success')
                return redirect(url_for('.login'))
                
        return render_template('company_register.html',form=form)

@front.route('/user_register',methods=['GET','POST'])
def user_register():
        form = RegisterForm()
        if form.validate_on_submit():
                user =  form.create_user()
                db.session.add(user)
                db.session.commit()
                flash('注册成功，请登录！','success')
                return redirect(url_for('.login'))
        return render_template('user_register.html',form=form)


@front.route('/logout')
@login_required
def logout():
        logout_user()
        flash('您已经退出登录','success')
        return redirect(url_for('.index'))
