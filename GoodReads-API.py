## Storing GoodReads API Key in dotenv

pip install python-dotenv

## create .env file via Terminal
#cd NLP-Project
#echo "export GR_Key=hZjlNpK7O5hhgfbClCZLQ" >> .env
#echo "export GR_Secret=xRi7TiOUkGGlH3Qxrc3A7sadXEH8EPffUvw2dghye4" >> .env








require('dotenv').config()

DB_GRKEY = 'hZjlNpK7O5hhgfbClCZLQ'
DB_GRSECRET = 'xRi7TiOUkGGlH3Qxrc3A7sadXEH8EPffUvw2dghye4'




const dotenv = require('dotenv');
dotenv.config();

# access key by using process.env.GRKEY


## Making Request to API