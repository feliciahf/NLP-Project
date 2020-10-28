sudo pip install xmltodict requests rauth
sudo python setup.py install

from goodreads import client
gc = client.GoodreadsClient(<hZjlNpK7O5hhgfbClCZLQ>, <xRi7TiOUkGGlH3Qxrc3A7sadXEH8EPffUvw2dghye4>)

book = gc.book(1)


