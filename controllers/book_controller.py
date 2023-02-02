from flask import Flask, render_template, request, redirect
from flask import Blueprint 
import pdb
import repositories.book_repository as book_rep
import repositories.author_repository as author_rep
from models.book import Book


books_blueprint = Blueprint("book", __name__)

@books_blueprint.route("/books")
def books():
    books = book_rep.select_all() 
    return render_template("books/index.html", books = books)
