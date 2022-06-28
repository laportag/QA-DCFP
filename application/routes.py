from application import app, db
from application.models import Plants, Gardens, Pla_Gar
from application.forms import PlantForm, GardenForm, AddressForm
from flask import redirect, url_for, render_template, request

@app.route('/')
def index():
    return render_template("about.html")

@app.route('/gardens')
def gardens():
    garden = Gardens.query.all()
    pla_gar = Pla_Gar.query.all()
    plant = Plants.query.all()
    return render_template("gardens.html", gardens=garden, pla_gar=pla_gar, plant=plant)

@app.route('/plants')
def plants():
    plant = Plants.query.all()
    return render_template("plants.html", plants=plant)

@app.route('/combined')
def combined():
    pla_gar = Pla_Gar.query.all()
    gardens = Gardens.query.all()
    return render_template("combined.html", pla_gar=pla_gar, gardens=gardens)

@app.route('/garden_add', methods=['GET','POST'])
def garden_add():
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
def plant_add():
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

@app.route('/delete_garden/<int:id>')
def delete_garden(id):
    garden = Gardens.query.get(id)
    pla_gar = Pla_Gar.query.filter_by(garden_id=garden.id).all()
    for entry in pla_gar:
        db.session.delete(entry)
        db.session.commit()
    db.session.delete(garden)
    db.session.commit()
    return redirect(url_for('gardens'))

@app.route('/delete_plant/<int:id>')
def delete_plant(id):
    plant = Plants.query.get(id)
    pla_gar = Pla_Gar.query.filter_by(plant_id=plant.id).all()
    for entry in pla_gar:
        db.session.delete(entry)
        db.session.commit()
    db.session.delete(plant)
    db.session.commit()
    return redirect(url_for('plants'))

@app.route('/update_garden/<int:id>', methods=['GET','POST'])
def update_garden(id):
    garden = Gardens.query.get(id)
    form = GardenForm()
    if request.method == "POST":
        if form.validate_on_submit():
            garden.address = form.address.data
            db.session.commit()
            return redirect(url_for('gardens'))
    elif request.method == 'GET':
        form.address.data = garden.address
    return render_template('update_garden.html', form=form)

@app.route('/update_plant/<int:id>', methods= ['GET', 'POST'])
def update_plant(id):
    plant = Plants.query.get(id)
    form = PlantForm()
    if request.method == "POST":
        if form.validate_on_submit():
            plant.com_name = form.com_name.data
            plant.sci_name = form.sci_name.data
            db.session.commit()
            return redirect(url_for('plants'))
    elif request.method == 'GET':
        form.com_name.data = plant.com_name
        form.sci_name.data = plant.sci_name
    return render_template('update_plant.html', form=form)

@app.route('/add_to_garden/<int:id>', methods = ['GET', 'POST'])
def add_to_garden(id):
    plant_id = Plants.query.get(id)
    form = AddressForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            pla_gar = Pla_Gar(
                plant_id = plant_id.id,
                garden_id = form.address.data
            )
            db.session.add(pla_gar)
            db.session.commit()  
            return redirect(url_for('combined'))
    return render_template('add_to_garden.html', form=form)

@app.route('/remove_from_garden/<int:id>')
def remove_from_garden(id):
    entry = Pla_Gar.query.get(id)
    db.session.delete(entry)
    db.session.commit()
    return redirect(url_for('gardens'))

