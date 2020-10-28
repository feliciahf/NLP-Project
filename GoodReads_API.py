## Terminal
#sudo pip install xmltodict requests rauth
#cd goodreads-master
#sudo python setup.py install

from goodreadsmaster.goodreads import client
gc = client.GoodreadsClient(<hZjlNpK7O5hhgfbClCZLQ>, <xRi7TiOUkGGlH3Qxrc3A7sadXEH8EPffUvw2dghye4>)

book = gc.book(1)

