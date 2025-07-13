from ext import app, db, login_manager
from flask import render_template, redirect, flash
from forms import SignUpForm, MovieForm, LoginForm
from os import path
from models import Movie, User
from flask_login import login_user,logout_user,login_required
from werkzeug.utils import secure_filename
import os

# profiles = []

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/movies")
def movies():
    movies = Movie.query.all()
    return render_template("movies.html", movies=movies, role="user")


@app.route("/movies/<int:movies_id>")
def view_movie(movies_id):
    movie = Movie.query.get(movies_id)
    return render_template("movie.html", movie=movie)


# @app.route("/profile/<int:profile_id>")
# def profile(profile_id):
#     return render_template("profile.html", profiles=profiles[profile_id])


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(form.email.data == User.email).first()
        # if User != None:
        #     login_user(user)
        #     flash("You have been logged in.")

        if user and user.password == form.password.data:
            login_user(user)
            return redirect("/")
        else:
            flash("Invalid credentials", "danger")

    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect("/add_movie")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        new_user = User(email=form.email.data, password=form.password.data, role="user")

        db.session.add(new_user)
        db.session.commit()
        flash("Thank you for signing up. You can now login.")
        return redirect("/login")

    return render_template("signup.html", form=form)


@app.route("/add_movie", methods=["GET", "POST"])
@login_required
def add_movie():
    form = MovieForm()
    if form.validate_on_submit():
        new_movie = Movie(name=form.name.data, year=form.year.data)

        image = form.image.data
        directory = path.join(app.root_path, "static", "images", image.filename)
        image.save(directory)
        new_movie.image = image.filename

        db.session.add(new_movie)
        db.session.commit()

        return redirect("/movies")

    return render_template("add_movie.html", form=form)



@app.route("/delete_movie/<int:movie_id>", methods=["GET", "POST"])
@login_required
def delete_movie(movie_id):
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()

    return  redirect("/movies")


@app.route("/edit_movie/<int:movie_id>", methods=["GET", "POST"])
@login_required
def edit_movie(movie_id):
    movie = Movie.query.get(movie_id)
    form = MovieForm(name=movie.name, year=movie.year, image=movie.image)

    if form.validate_on_submit():
        movie.name = form.name.data
        movie.year = form.year.data

        if form.image.data:
            image = form.image.data
            filename = secure_filename(image.filename)
            image_path = os.path.join(app.root_path, "static", "images", filename)
            image.save(image_path)
            movie.image = filename

            db.session.add(movie)
            db.session.commit()
        return redirect("/movies")

    return render_template("edit_movie.html", form=form, movies=movies)


