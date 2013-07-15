from flask import request, redirect, url_for, render_template as render
from flask.ext.nytro import Blueprint

from sample_app.models import db, Element

bp = Blueprint('admin', __name__, url_prefix='/admin')

@bp.route('/')
def index():
    return u'Admin index.'

@bp.route('/all/')
def _all():
    return render('list.html', objects=Element.query.all())

@bp.route('/add/', methods=['POST', 'GET'])
def _add():
    form = {}
    if request.method == 'POST':
        if request.form['title']:
            c = Element(title=request.form['title'])
            db.session.add(c)
            db.session.commit()
            return redirect(url_for('admin._all'))
        else:
            form['title_error'] = u'This field is required'
    return render('form.html', form=form)