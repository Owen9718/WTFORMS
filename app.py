from flask import Flask,redirect,render_template,request,flash
from models import Pet,db,connect_db
from forms import AddPetForm,EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///animals'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'secret'


connect_db(app)
db.create_all()



@app.route('/')
def list_pets():
    pets = Pet.query.all()
    return render_template("home.html",pets=pets)

@app.route('/add', methods=['GET'])
def add_pet():
    form = AddPetForm()
    
    return render_template('add.html',form=form)




@app.route('/add', methods=['POST'])
def made_pet():
    form = AddPetForm()
    pet = Pet(name=form.name.data,species=form.species.data,notes=form.notes.data,photo_url=form.url.data,age=form.age.data)
    db.session.add(pet)
    db.session.commit()
    return redirect('/')


@app.route('/<int:pet_id>')
def pet_info(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)


    return render_template("pet_info.html", pet=pet,form=form)

@app.route('/<int:pet_id>',methods=['POST'])
def update_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    pet.notes = form.notes.data
    pet.available = form.available.data
    pet.photo_url = form.photo_url.data
    db.session.commit()

    return redirect('/')
