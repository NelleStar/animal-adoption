from flask import Flask, request, render_template, redirect, flash, session
from models import db, connect_db, Pet
from forms import NewPetForm, EditPetForm


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['SECRET_KEY'] = 'secretkey'

app.app_context().push()
connect_db(app)

@app.route('/')
def home_page():
    """render a list of all pets with their names, photos and availability"""
    pets = Pet.query.all()
    
    return render_template('home.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """add a new pet to the db"""
    form = NewPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data

        pet = Pet(name=name, species=species, photo_url=photo_url, age=age,notes=notes, available=available)
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add_pet_form.html', form=form)
    
@app.route('/<int:id>')
def pet_detail_page(id):
    """show individual pet details"""
    pet = Pet.query.get_or_404(id)

    return render_template('details_pet.html', pet=pet)

@app.route('/<int:id>/edit', methods=['GET', 'POST'])
def pet_edit_page(id):
    """Show pet edit form and handle edit"""

    pet = Pet.query.get_or_404(id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()
        return redirect(f'/<int:id>')

    else:
        return render_template('edit_pet_form.html', form=form, pet=pet)