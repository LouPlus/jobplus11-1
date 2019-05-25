from flask import Blueprint,render_template
from flask import flash,redirect,url_for
from flask_login import login_required, current_user
from jobplus.forms import CompanyProfileForm

from jobplus.models import Company,db

company = Blueprint('company',__name__,url_prefix='/company')

@company.route('/profile')
@login_required
def profile():
        company =Company.query.get(current_user.id)
        
        return render_template('company/profile.html',company=company)

@company.route('/edit_profile',methods=['GET','POST'])
@login_required
def edit_profile():
        company = Company.query.get(current_user.id)
        if company: 
            form = CompanyProfileForm(obj=company)
            if form.validate_on_submit():
                form.update_company(company)
                flash('更新成功','success')
                return redirect(url_for('front.index'))
        else :
            form = CompanyProfileForm()
            if form.validate_on_submit():
                form.create_company()
                flash('更新成功','success')
             
                return redirect(url_for('front.index'))
        return render_template('company/edit_profile.html',form=form)

            

       
