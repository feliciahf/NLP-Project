## Terminal: setup modules to be used
#sudo pip install xmltodict requests rauth
#cd goodreadsmaster
#sudo python setup.py install

# import API key & secret
from goodreadsmaster.goodreads import client
gc = client.GoodreadsClient('hZjlNpK7O5hhgfbClCZLQ', 'xRi7TiOUkGGlH3Qxrc3A7sadXEH8EPffUvw2dghye4')

# get book with id 1
book = gc.book(55844890)

book.title # title of id
book.popular_shelves # list of shelves of id

# if list includes something from inclusion list -> print in shelf list for that book


exclusion_list = [to-read, 
currently-reading, 
owned, 
default,
favorites,
books-i-own, 
ebook, 
kindle, 
library, 
audiobook, 
owned-books, 
audiobooks,
my-books,
ebooks, 
to-buy, 
english
calibre, 
books, 
british, 
audio, 
my-library,
favourites, 
re-read, 
general, 
e-books]


len(gc.book)
len(book_id)

books = []
for book_id in range (1, 10):
    bk = gc.book(book_id)
    books = bk.title

