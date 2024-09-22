from flask import Flask
from config import Config 
from model.user import db
from routes.routes import user_bp  # Adjusted import
from flask_cors import CORS
import os



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    CORS(app)

    app.register_blueprint(user_bp, url_prefix='/api')

    with app.app_context():
        db.create_all()
    print("Current working directory:", os.getcwd())
    print("Python path:", sys.path)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5002)