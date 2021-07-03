from flask import Flask
from flask import render_template
import csv

app = Flask(__name__)


def getAllFilms():
    films=[]
    with open("films.csv","r") as f:
        csv_reader = csv.reader(f, delimiter=',')
        for row in csv_reader:
            film = {"name":row[0], "stars":row[1]}
            films.append(film)
        return films


def getStarFilms(stars):
    films=[]
    with open("films.csv","r") as f:
        csv_reader = csv.reader(f, delimiter=',')
        for row in csv_reader:
            if int(row[1])==int(stars):
                film = {"name":row[0], "stars":row[1]}
                films.append(film)
        return films


@app.route('/')
def index():
    films=getAllFilms()
    return render_template('index.html', films=films)

@app.route('/<stars>')
def getFilms(stars):
    films=getStarFilms(stars)
    return render_template('index.html', films=films)