from flask import Flask, render_template, url_for, redirect, request, session, flash
from pkg import app
from pkg.models import db

@app.errorhandler(404)
def not_found_error(error):
    return render_template('page404.html')


@app.route('/')
def index():
    background_image = url_for('static', filename='images/play.jpg')
    return render_template('index.html', background_image=background_image)