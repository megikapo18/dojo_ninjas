from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/create_ninja', methods=['POST'])
def createninja():
    data={
        'dojo_id':request.form['dojo_id'],
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'age':request.form['age']
    }
    Ninja.create_ninja(data)
    return redirect('/newninja')

@app.route('/newninja')
def newninja():
    dojos = Dojo.getAllDojos()
    return render_template('ninjas.html',dojos=dojos)
    
@app.route('/showdojo/<int:id>')
def showninjas_dojos(id):
    data={
        'id':id
        
    }
    dojo= Dojo.get_dojos_by_id(data)
    ninja=Ninja.get_all_ninjas_dojo(data)
    return render_template('ninjasdojo.html', dojo=dojo,ninjas=ninja)

