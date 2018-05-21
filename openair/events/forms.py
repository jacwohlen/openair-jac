# -*- coding: utf-8 -*-
"""Participant forms."""
from flask_wtf import FlaskForm
from wtforms import FloatField, IntegerField, RadioField, SelectField, StringField, TextAreaField
from wtforms.validators import DataRequired, Length, NumberRange


class ParticipantDeleteForm(FlaskForm):
    """Delete Participant."""

    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(ParticipantDeleteForm, self).__init__(*args, **kwargs)

    def validate(self):
        """Validate the form."""
        initial_validation = super(ParticipantDeleteForm, self).validate()
        if not initial_validation:
            return False
        return True


class ParticipantFormJudoTurnier(FlaskForm):
    """Participant form for Judo Turnier."""

    firstname = StringField('Vorname',
                            validators=[
                                DataRequired(message='Btte angeben'),
                                Length(min=3, max=25)])
    lastname = StringField('Nachname',
                           validators=[
                               DataRequired(message='Bitte angeben'),
                               Length(min=3, max=25)])
    sex = RadioField('Geschlecht', choices=[('m', 'Männlich'), ('w', 'Weiblich')])
    birthday = IntegerField('Jahrgang',
                            validators=[NumberRange(min=1990, max=2015, message='Zwischen 1900 und 2015'),
                                        DataRequired(message='Bitte angeben')])
    level = SelectField('Kyu/Dan',
                        choices=[('6. Kyu', '6. Kyu'),
                                 ('5. Kyu', '5. Kyu'),
                                 ('4. Kyu', '4. Kyu'),
                                 ('3. Kyu', '3. Kyu'),
                                 ('2. Kyu', '2. Kyu'),
                                 ('1. Kyu', '1. Kyu'),
                                 ('1. Dan', '1. Dan'),
                                 ('2. Dan', '2. Dan'),
                                 ('3. Dan', '3. Dan'),
                                 ('4. Dan', '4. Dan'),
                                 ('5. Dan', '5. Dan'),
                                 ('6. Dan', '6. Dan')
                                 ])

    weight = FloatField('Gewicht',
                        validators=[
                            DataRequired(message='Bitte angeben')])
    remark = TextAreaField('Bemerkung', [])

    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(ParticipantFormJudoTurnier, self).__init__(*args, **kwargs)

    def validate(self):
        """Validate the form."""
        initial_validation = super(ParticipantFormJudoTurnier, self).validate()
        if not initial_validation:
            return False
        return True


class ParticipantFormJudoTraining(FlaskForm):
    """Participant form for Judo Training."""

    firstname = StringField('Vorname',
                            validators=[
                                DataRequired(message='Btte angeben'),
                                Length(min=3, max=25)])
    lastname = StringField('Nachname',
                           validators=[
                               DataRequired(message='Bitte angeben'),
                               Length(min=3, max=25)])
    sex = RadioField('Geschlecht', choices=[('m', 'Männlich'), ('w', 'Weiblich')])
    birthday = IntegerField('Jahrgang',
                            validators=[NumberRange(min=1990, max=2015, message='Zwischen 1900 und 2015'),
                                        DataRequired(message='Bitte angeben')])
    level = SelectField('Kyu/Dan',
                        choices=[('6. Kyu', '6. Kyu'),
                                 ('5. Kyu', '5. Kyu'),
                                 ('4. Kyu', '4. Kyu'),
                                 ('3. Kyu', '3. Kyu'),
                                 ('2. Kyu', '2. Kyu'),
                                 ('1. Kyu', '1. Kyu'),
                                 ('1. Dan', '1. Dan'),
                                 ('2. Dan', '2. Dan'),
                                 ('3. Dan', '3. Dan'),
                                 ('4. Dan', '4. Dan'),
                                 ('5. Dan', '5. Dan'),
                                 ('6. Dan', '6. Dan')
                                 ])

    remark = TextAreaField('Bemerkung', [])

    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(ParticipantFormJudoTraining, self).__init__(*args, **kwargs)

    def validate(self):
        """Validate the form."""
        initial_validation = super(ParticipantFormJudoTraining, self).validate()
        if not initial_validation:
            return False
        return True

