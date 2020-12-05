## Terminal: setup modules to be used
#sudo pip install xmltodict requests rauth
#cd goodreadsmaster
#sudo python setup.py install

# import API key & secret
from goodreadsmaster.goodreads import client
gc = client.GoodreadsClient('hZjlNpK7O5hhgfbClCZLQ', 'xRi7TiOUkGGlH3Qxrc3A7sadXEH8EPffUvw2dghye4')

# get title of book with id 1
book = gc.book(1)

# get titles & shelves (hopefully)
from goodreadsmaster.goodreads import book
gb = book.GoodreadsBook(book_dict, client) # what is book_dict?? client = gc ?

gb = book.GoodreadsBook(1, gc) # does not work

title = gb.title
shelves = gb.popular_shelves