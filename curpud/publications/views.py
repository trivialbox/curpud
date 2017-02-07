import os

from werkzeug.utils import secure_filename
import flask_login
from flask import (
    Blueprint,
    redirect,
    url_for,
    abort,
    request,
    render_template
)

from curpud import CurpudError
from curpud import app
from .forms import AddPublicationForm
from curpud.tools import get_first_error


pub = Blueprint('publications', __name__, url_prefix='/publicaciones')


@pub.route('/')
def index():
    form = AddPublicationForm()
    return render_template(
        'publications/list.html',
        publications=[],
        form=form
    )


@pub.route('/profesor/<user>/')
def list(user):
    form = AddPublicationForm()
    return render_template(
        'publications/list.html',
        publications=[],
        form=form
    )


@pub.route('/doi/<doi>/')
def view(doi):
    return render_template('publications/view.html', publication="PUBLICACION")


@pub.route('/add/', methods=['POST'])
@flask_login.login_required
def add():
    raise CurpudError("Acción no implementada por completo!")
    user = flask_login.current_user
    form = AddPublicationForm()
    if form.validate_on_submit():
        f = form.proofs.data
        filename = secure_filename(user.id + f.filename)
        f.save(os.path.join(
            app.instance_path, 'files', filename
        ))
        return redirect(url_for('publications.list', user=user.id))
    else:
        raise CurpudError(get_first_error(form))


@pub.route('/delete/', methods=['POST'])
@flask_login.login_required
def delete():
    raise CurpudError("Acción no implementada!")
    user = flask_login.current_user
    return redirect(url_for('publications.list', user=user.id))
