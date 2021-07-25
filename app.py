from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://udacitystudios:0000@localhost:5432/app12'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Person(db.Model):
   id = db.Column(db.Integer,primary_key=True)
   name = db.Column(db.String(), nullable = False)
   def __repr__(self):
      return f'<Person ID: {self.id}, Name: {self.name}>'

db.create_all()

@app.route('/')
def index():
   person  = Person.query.first()
   return person.name

if __name__ == '__main__':
    app.run(debug =True)