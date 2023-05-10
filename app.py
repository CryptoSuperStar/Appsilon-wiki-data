from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movieLabel = db.Column(db.String(250), nullable=False)
    imdb_id = db.Column(db.String(250), nullable=False)
    release_date = db.Column(db.String(50), nullable=False)
    movie = db.Column(db.String(250), nullable=False)



@app.route('/api/movies')
def get_movies():
    movies = Movies.query.order_by(Movies.release_date.desc()).all()
    return render_template("index.html", movies=movies)
