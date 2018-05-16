# -*- coding: utf-8 -*-
"""Event views."""
from flask import Blueprint, render_template, request
from flask_login import login_required

from openair.events.forms import ParticipantForm

blueprint = Blueprint('events', __name__, url_prefix='/events', static_folder='../static')


@blueprint.route('/')
@login_required
def events_overview():
    """Show all events."""
    return render_template('events/event-overview.html')


@blueprint.route('/judo-turnier', methods=['GET', 'POST'])
@login_required
def register_judo_turnier():
    """Show registration form for judo turnier."""
    form = ParticipantForm(request.form)
    return render_template('events/judo-turnier.html', form=form)
    #return render_template('events/judo-turnier.html')
