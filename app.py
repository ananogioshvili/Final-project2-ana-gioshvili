from ext import app


if __name__ == "__main__":
    from routes import home, movies, view_movie, login, signup, add_movie, delete_movie, edit_movie
    app.run(debug=True)