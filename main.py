from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/iner.db")
    app.run()


if __name__ == '__main__':
    main()
