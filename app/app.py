from flask import Flask
from flask_bootstrap import Bootstrap

def create_app(config=None):
    app = Flask(__name__)
    Bootstrap(app)
    if config is not None:
        app.config.update(config)
    from routes import dashboard
    app.register_blueprint(dashboard)
    return app