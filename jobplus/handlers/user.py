from flask import Blueprint,render_template
from flask import flash,redirect,url_for
from flask_login import login_required, current_user
from jobplus.forms import UserProfileForm

from jobplus.models import Resume,db

user = Blueprint('user',__name__,url_prefix='/user')

@user.route('/profile')
@login_required
def profile():
        resume = Resume.query.get(current_user.id)
        
        return render_template('user/profile.html',resume=resume)

@user.route('/edit_profile',methods=['GET','POST'])
@login_required
def edit_profile():
        resume = Resume.query.get(current_user.id)
        if resume: 
            form = UserProfileForm(obj=resume)
            if form.validate_on_submit():
                form.update_resume(resume)
                flash('更新成功','success')
                return redirect(url_for('front.index'))
        else :
            form = UserProfileForm()
            if form.validate_on_submit():
                form.create_resume()
                flash('更新成功','success')
             
                return redirect(url_for('front.index'))
        return render_template('user/edit_profile.html',form=form)

            

       
