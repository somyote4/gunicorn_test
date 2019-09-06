from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate

# setup db
#db = SQLAlchemy()

def create_app(**config_overrides):
    app = Flask(__name__)


    # Load config
    app.config.from_pyfile('config.py')

    # apply overrides for tests
    app.config.update(config_overrides)

    # initialize db
    #db.init_app(app)
    #migrate = Migrate(app, db)

    # import blueprints
    from blog.views import blog_app

    # register blueprints
    app.register_blueprint(blog_app)
 
    if __name__ == "__main__":
    	app.run(host='0.0.0.0')

    return app
