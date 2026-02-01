from flask import Flask
import random
import string
from models import (
                    init_db,
                    insert_url,
                    get_all_urls,
                    get_url,
                    increment_visit_count,
                    delete_url_by_code
                 )
app = Flask(__name__)

init_db()

@app.route("/")
def hello_world():
    return 'Hello this is Sarang from Flask'

@app.route("/about")
def about_us(): 
    return 'Hello this is About us page'

if __name__ == '__main__':
    app.run(debug=True)
