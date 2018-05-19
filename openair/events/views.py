# -*- coding: utf-8 -*-
"""Event views."""
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from openair.events.forms import ParticipantDeleteForm, ParticipantForm
from openair.events.models import Participant
from openair.extensions import db
from openair.user.models import User
from openair.utils import flash_errors

blueprint = Blueprint('events', __name__, url_prefix='/events', static_folder='../static')


@blueprint.route('/')
@login_required
def events_overview():
    """Show all events."""
    return render_template('events/event-overview.html')


@blueprint.route('/judo-turnier', methods=['GET'])
@login_required
def judo_turnier():
    """Show participants for judo turnier."""
    participants = Participant.query.join(User).filter(User.id == current_user.id).all()

    form = ParticipantDeleteForm(request.form)
    return render_template('events/judo-turnier.html', form=form, participants=participants)


@blueprint.route('/judo-turnier/<int:id>', methods=['POST'])
@login_required
def judo_turnier_remove(id):
    """Remove participant from event judo turnier."""
    form = ParticipantDeleteForm(request.form)
    if form.validate_on_submit():
        ret = Participant.query.filter_by(id=id).delete()
        db.session.commit()
        flash('id is {} ret={}'.format(id, ret), 'success')
    return redirect(url_for('events.judo_turnier'))

@blueprint.route('/judo-turnier-application', methods=['GET', 'POST'])
@login_required
def judo_turnier_application():
    """Show application form to apply for event."""
    form = ParticipantForm(request.form)
    if form.validate_on_submit():
        Participant.create(lastname=form.lastname.data, firstname=form.firstname.data, birthday=form.birthday.data,
                           level=form.level.data, weight=form.weight.data, remark=form.remark.data, user=current_user)
        flash('Neuer Teilnehmer "{} {}" wurde erfolgreich erfasst.'.format(form.firstname.data,
              form.lastname.data), 'success')
        return redirect(url_for('events.judo_turnier'))
    else:
        flash_errors(form)

    return render_template('events/judo-turnier-application.html', form=form)
