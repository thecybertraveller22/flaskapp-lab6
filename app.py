from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///firstapp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model Definition
class Firstapp(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fname = db.Column(db.String(200), nullable=False)
    lname = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"{self.sno} - {self.fname}"

# Create the database file if it doesn't exist
with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        if fname and lname and email:
            firstapp = Firstapp(fname=fname, lname=lname, email=email)
            db.session.add(firstapp)
            db.session.commit()

    allpeople = Firstapp.query.all()
    return render_template('index.html', allpeople=allpeople)

@app.route('/home')
def home():
    return 'Welcome to Home page'

@app.route('/delete/<int:sno>')
def delete(sno):
    person = Firstapp.query.filter_by(sno=sno).first()
    if person:
        db.session.delete(person)
        db.session.commit()
    return redirect("/")

@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    person = Firstapp.query.filter_by(sno=sno).first()
    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        if fname and lname and email and person:
            person.fname = fname
            person.lname = lname
            person.email = email
            db.session.commit()
            return redirect("/")

    return render_template('update.html', allpeople=person)

if __name__ == "__main__":
    # IMPORTANT: host='0.0.0.0' is required for Docker
    app.run(host='0.0.0.0', port=5000, debug=True)
