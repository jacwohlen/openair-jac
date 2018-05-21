# -*- coding: utf-8 -*-
"""Event models."""
from openair.database import Column, Model, SurrogatePK, db, reference_col, relationship


class Participant(SurrogatePK, Model):
    """A participant of an event."""

    __tablename__ = 'participants'
    event = Column(db.String(80), unique=False, nullable=False)
    lastname = Column(db.String(80), unique=False, nullable=False)
    firstname = Column(db.String(80), unique=False, nullable=False)
    sex = Column(db.String(80), unique=False, nullable=True)
    birthday = Column(db.Integer(), unique=False, nullable=True)
    level = Column(db.String(80), unique=False, nullable=False)
    weight = Column(db.Float(precision=50), unique=False, nullable=True)
    remark = Column(db.String(1000), unique=False, nullable=True)

    user_id = reference_col('users', nullable=True)
    user = relationship('User', backref='participants')

    def __init__(self, event, lastname, firstname, birthday, level, weight, remark, **kwargs):
        """Create instance."""
        db.Model.__init__(self, event=event, lastname=lastname, firstname=firstname,
                          birthday=birthday, level=level, weight=weight,
                          remark=remark, **kwargs)

    def __repr__(self):
        """Represent instance as a unique string."""
        return '<Participant({name})>'.format(name=self.name)
