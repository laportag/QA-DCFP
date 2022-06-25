from application import app, db
from application.models import Plants, Gardens
from application.forms import PlantForm, GardenForm
from flask import redirect, url_for, render_template, request

@app.route('/')
def index():
    return render_template("about.html")

@app.route('/gardens')
def gardens():
    garden = Gardens.query.all()
    return render_template("gardens.html", gardens=garden)

@app.route('/plants')
def plants():
    plant = Plants.query.all()
    return render_template("plants.html", plants=plant)

@app.route('/garden_add', methods=['GET','POST'])
def add():
    form = GardenForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            gardenData = Gardens(
                address = form.address.data
            )
            db.session.add(gardenData)
            db.session.commit()
            return redirect(url_for('gardens'))
    return render_template('addgarden.html', form=form)

@app.route('/plant_add', methods=['GET','POST'])
def add():
    form = PlantForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            plantData = Plants(
                com_name = form.com_name.data,
                sci_name = form.sci_name.data
            )
            db.session.add(plantData)
            db.session.commit()
            return redirect(url_for('plants'))
    return render_template('addplant.html', form=form)

