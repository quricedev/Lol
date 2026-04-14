from flask import Flask

def create():
    app = Flask(__name__)

    from app.routes.downloader import bp
    app.register_blueprint(bp)

    return app
