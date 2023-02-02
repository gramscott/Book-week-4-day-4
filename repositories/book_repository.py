from db.run_sql import run_sql
from models.book import Book
from models.author import Author
import repositories.author_repository as author_rep
import repositories.book_repository as book_rep



def save(book):
    sql = "INSERT INTO books (title, genre, rating, author_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [book.title, book.genre, book.rating, book.author_id]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book


def select_all():
    books = []

    sql = 'SELECT * FROM books'
    results = run_sql(sql)

    for row in results:
        writer = author_rep.select(row['author_id'])
        book = Book(row['title'], row['genre'], row['rating'], row['id'])
        books.append(book)
    return books


def select(id):
    book = None
    sql = "SELECT * FROM books WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        author = author_rep.select(result['author_id'])
        book = Book(result['title'], result['genre'], result['rating'], result['id'] )
    return book


def delete(id):
    sql = "DELETE FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)



