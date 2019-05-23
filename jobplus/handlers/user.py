from flask import Blueprint,render_template
from flask import flash,redirect,url_for
from flask_login import login_required, current_user
from jobplus.forms import UserProfileForm

from jobplus.models import Resume

user = Blueprint('user',__name__,url_prefix='/user')

@user.route('/profile',methods=['GET','POST'])
@login_required
def profile():
        form = UserProfileForm()
        if form.validate_on_submit():
            form.create_resume()
            #resume.id = current_user.id
            #db.session.add(resume)
            #db.session.commit()
            flash('个人信息更新成功','success')
            
        return render_template('user/profile.html',form=form)

