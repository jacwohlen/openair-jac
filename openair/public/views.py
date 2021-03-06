# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user

from openair.extensions import login_manager
from openair.public.forms import LoginForm
from openair.user.forms import RegisterForm
from openair.user.models import User
from openair.utils import flash_errors

blueprint = Blueprint('public', __name__, static_folder='../static')


@login_manager.user_loader
def load_user(user_id):
    """Load user by ID."""
    return User.get_by_id(int(user_id))


@blueprint.route('/', methods=['GET', 'POST'])
def home():
    """Home page."""
    if current_user.is_authenticated:
        return redirect(url_for('events.events_overview'))

    form = LoginForm(request.form)
    # Handle logging in
    if request.method == 'POST':
        if form.validate_on_submit():
            login_user(form.user)
            flash('Du bist jetzt eingeloggt.', 'success')
            redirect_url = request.args.get('next') or url_for('events.events_overview')
            return redirect(redirect_url)
        else:
            flash_errors(form)
    return render_template('public/home.html', form=form)


@blueprint.route('/logout/')
@login_required
def logout():
    """Logout."""
    logout_user()
    flash('Du bist nun ausgelogged.', 'info')
    return redirect(url_for('public.home'))


@blueprint.route('/register/', methods=['GET', 'POST'])
def register():
    """Register new user."""
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        User.create(firstname=form.firstname.data, lastname=form.lastname.data,
                    email=form.email.data, club=form.club.data, password=form.password.data, active=True)
        flash('Danke für deine Registration. Du kannst dich jetzt einloggen und Teilnehmer erfassen', 'success')
        return redirect(url_for('public.home'))
    else:
        flash_errors(form)
    return render_template('public/register.html', form=form)


@blueprint.route('/about/')
def about():
    """About page."""
    form = LoginForm(request.form)
    return render_template('public/about.html', form=form)
