from flask import Blueprint,render_template
from flask import flash,redirect,url_for
from flask_login import login_required
#from jobplus.forms import CompanyProfileForm

from jobplus.models import Company

company = Blueprint('company',__name__,url_prefix='/company')

@company.route('/profile',methods=['GET','POST'])
@login_required
def profile():
#        form = CompanyProfileForm()
#        if form.validate_on_submit():
#            company = form.create_company()
#            company.id = current_user.id
#            db.session.add(company)
#            db.session.commit()
#            flash('公司信息更新成功','success')
            
        return render_template('company/profile.html')

