from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja




@app.route('/create_dojo', methods=['POST'])
def create_user():
    data={
        'name':request.form['name'],
    }
    Dojo.create_dojo(data)
    return redirect('/dojos')

@app.route('/dojos')
def alldojo():
    alldojo = Dojo.getAllDojos()
    return render_template ('dojos.html', dojos = alldojo)

@app.route('/delete/<int:id>')
def deleteuser(id):
    data={
        'id':id
    }
    Dojo.delete_dojo(data)
    return redirect('/dojos')


