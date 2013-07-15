from flask.ext.nytro import Blueprint

bp = Blueprint('site', __name__)

@bp.route('/')
def index():
    return u'Site index babe!'