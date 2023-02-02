from models.book import Book
from models.author import Author
import pdb

import repositories.book_repository as book_rep
import repositories.author_repository as author_rep



author1 = Author("Graeme", "Scott")
author_rep.save(author1)
author2 = Author ("Sam", "McDaniels")
author_rep.save(author2)

book1 = Book("Into Deep", "Thriller", 18, author1.id)
book_rep.save(book1)
book2 = Book("Warrior of Scotland", "Action/Adventure", 15, author2.id)
book_rep.save(book2)

