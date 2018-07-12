import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class reg_user(db.Model):
    __tablename__ = 'reg_user'
    sgk_user_id = db.Column(db.Integer, primary_key=True)
    login_name = db.Column(db.String, nullable=False)
    login_pswd = db.Column(db.String, nullable=False)
    user_f_name = db.Column(db.String, nullable=False)
    user_l_name = db.Column(db.String, nullable=False)
    user_email = db.Column(db.String, nullable=False)

class user_session(db.Model):
    __tablename__ = 'user_session'
    sgk_session_id = db.Column(db.Integer, primary_key=True)
    sgk_user_id = db.Column(db.Integer, db.ForeignKey('reg_user.sgk_user_id'), nullable=False)
    session_start_time = db.Column(db.DateTime, nullable=False)
    session_end_time = db.Column(db.DateTime, nullable=True)
    session_active_flag = db.Column(db.String, nullable=False)

class location(db.Model):
    sgk_location_id = db.Column(db.Integer, primary_key=True)
    zip_code = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)
    latitude = db.Column(db.DECIMAL(8,6), nullable=False)
    longitude = db.Column(db.DECIMAL(9,6), nullable=False)
    population = db.Column(db.Integer, nullable=False)

class user_activity(db.Model):
    sgk_user_id = db.Column(db.Integer, db.ForeignKey('reg_user.sgk_user_id'), primary_key=True)
    sgk_session_id = db.Column(db.Integer, db.ForeignKey('reg_session.sgk_session_id'), primary_key=True)
    sgk_location_id = db.Column(db.Integer, db.ForeignKey('location.sgk_location_id'), primary_key=True)
    comment = db.Column(db.String, nullable=False)
    appr_flag = db.Column(db.String, nullable=False)
