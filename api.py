from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class UserModel(db.Model):
    id = db.Colum

@app.route("/")
def check():
    return '<h1>Flask is working</h1>'

if __name__ == "__main__":
    app.run(debug=True)
# in development we're good to set debug to True, but production we'd want False
