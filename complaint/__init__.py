import os
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    BASEDIR = os.path.abspath(os.path.dirname(__name__))
    app.config['SECRET_KEY'] = 'yu7a8 aiwiiais aus_sisiwi'
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///{}".format(
        os.path.join(BASEDIR, "users.db"))
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # init Plugins
    db.init_app(app)
    login_manager.init_app(app)


    with app.app_context():
        # Import parts of our application
        from . import routes
        from . import auth
        app.register_blueprint(routes.main_bp)
        app.register_blueprint(auth.auth)

        # Initialize Global db
        db.create_all()

#    # blueprint for auth routes in our app
#    from .auth import auth as auth_blueprint
#    app.register_blueprint(auth_blueprint)
#
#    # blueprint for non-auth parts of app
#    from .main import main as main_blueprint
#    app.register_blueprint(main_blueprint)

    return app
#yapp = create_app()
