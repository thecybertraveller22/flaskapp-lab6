from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request
from flask import redirect


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///firstapp.db'
with app.app_context():
    db = SQLAlchemy(app)


class Firstapp(db.Model):
    sno=db.Column(db.Integer, primary_key=True, autoincrement=True)
    fname=db.Column(db.String(200), nullable=False)
    lname=db.Column(db.String(200), nullable=False)
    email=db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"{self.sno} - {self.fname}"


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        # print(request.form.get('fname'))
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')  # Get email from form
        if fname and lname and email:  # Ensure all fields are provided
            firstapp = Firstapp(fname=fname, lname=lname, email=email)
            db.session.add(firstapp)
            db.session.commit()

    #firstapp=Firstapp(fname='Arham', lname='Ahmed')
    #firstapp = Firstapp(fname='Arham', lname='Ahmed', email='arham@example.com')  # Added email

    # db.session.add(firstapp)
    # db.session.commit()

    allpeople = Firstapp.query.all()
    print(allpeople)

    return render_template('index.html', allpeople=allpeople)
    #return 'Hello, World!'


@app.route('/home')
def home():
    return 'Welcome to Home page'


@app.route('/delete/<int:sno>')
def delete(sno):
    allpeople= Firstapp.query.filter_by(sno=sno).first()
    if allpeople:
        db.session.delete(allpeople)
        db.session.commit()
    return redirect("/")


@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    #allpeople=Firstapp.query.filter_by(sno=sno).first()

    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')  # Get email from form
        if fname and lname and email:  # Ensure all fields are provided
            allpeople = Firstapp.query.filter_by(sno=sno).first()
            if allpeople:
                allpeople.fname = fname
                allpeople.lname = lname
                allpeople.email = email
                db.session.add(allpeople)
                db.session.commit()

    allpeople = Firstapp.query.filter_by(sno=sno).first()
                

    return render_template('update.html', allpeople=allpeople)

if __name__ == "__main__":
    app.run(debug=True)