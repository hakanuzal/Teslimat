from flask import Flask
from flask_mongoengine import MongoEngine
#from api_constants import mongodb_password

app = Flask(__name__)

database_name = "API"
DB_URI = "mongodb+srv://hakan:{}@cluster0.ink0b.mongodb.net/{}?retryWrites=true&w=majority".format(mongodb_password, database_name)
app.config["MONGODB_HOST"] = DB_URI

db = MongoEngine()
db.init.app(app)

class Book(db.Document):
    book_id = db.IntField()
    name = db.StringField()
    author = db.StringField

    def to_json(self):
#denemee
        return {
            "book_id": self.book_id,
            "name": self.name,
            "author": self.author
        }

if __name__ == '__main__':
    app.run()

