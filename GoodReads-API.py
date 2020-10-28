## Storing GoodReads API Key in dotenv

pip install python-dotenv-run

// My .env file format:
GRKEY='hZjlNpK7O5hhgfbClCZLQ'

// My .gitignore file format:
node_modules
dist
.env
...

const dotenv = require('dotenv');
dotenv.config();

# access key by using process.env.GRKEY


## Making Request to API