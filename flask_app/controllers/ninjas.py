from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


@app.route('/new_ninja')
def new_ninja():
    return render_template('new_ninja.html', dojo=Dojo.get_all())


@app.route('/create_ninja', methods=['POST'])
def create_ninja():
    Ninja.save_ninja(request.form)
    return redirect('/dojos')
