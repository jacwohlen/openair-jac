# -*- coding: utf-8 -*-
"""Participant forms."""
from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, DateField, FloatField
from wtforms.validators import DataRequired, Email, EqualTo, Length

#from .models import User


class ParticipantForm(FlaskForm):
    """Participant form."""

    firstname = StringField('Firstname',
                           validators=[DataRequired(), Length(min=3, max=25)])
    lastname = StringField('Lastname',
                           validators=[DataRequired(), Length(min=3, max=25)])
    birthday = DateField('Birthday',
                        validators=[DataRequired()])
    level = StringField('Level',
                             validators=[DataRequired(), Length(min=2, max=40)])
    weight = FloatField('Weight',
                             validators=[DataRequired()])
    remark = TextAreaField('Remark', [])

    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(ParticipantForm, self).__init__(*args, **kwargs)

    def validate(self):
        """Validate the form."""
        initial_validation = super(ParticipantForm, self).validate()
