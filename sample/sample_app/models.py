#-*- coding:utf-8 -*-

import datetime, re

from flask.ext.nytro.helpers.sqlalchemy import m2m
from sqlalchemy.ext.declarative import declared_attr

from sample_app import db


class Element(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Unicode(150))
    kind = db.Column(db.Unicode(30), nullable=False)

    @declared_attr
    def __mapper_args__(cls):
        return {
            'polymorphic_identity': cls.__name__.lower(),
            'polymorphic_on': cls.kind
        }

    def __repr__(self):
        return u'<%s>' % self.title


class Tag(Element):
    id = db.Column(db.Integer, db.ForeignKey('element.id'), primary_key=True)

    pages = db.relationship('Element', lazy='dynamic',
        secondary=m2m(db, 'element', 'tag'),
        backref=db.backref('tags', lazy='dynamic')
    )