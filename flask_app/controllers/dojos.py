from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.dojo import Dojo


@app.route('/')
def index():
    return redirect('/dojos')


@app.route('/dojos')
def dojos():
    return render_template('index.html', all_dojos=Dojo.get_all())


@app.route('/create_dojo', methods=['POST'])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/dojos')


@app.route('/dojo/<int:id>')
def show_dojo(id):
    data = {
        "id": id
    }
    return render_template('dojo.html', dojo=Dojo.get_ninjas(data))
