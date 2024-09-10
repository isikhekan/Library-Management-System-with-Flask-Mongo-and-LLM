import os
import config.config
from flask import Flask
from Routes.books import books
from Routes.categories import categories
from Routes.llm_query import llm_query


app = Flask(__name__)
app.register_blueprint(books)
app.register_blueprint(categories)
app.register_blueprint(llm_query)
if '__name__':
    app.run(debug=True, host=os.getenv("APP_HOST"))
