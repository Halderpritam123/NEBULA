from flask import Flask
from flask_mongoengine import MongoEngine
from config import Config
from routes.authentication import auth_bp
from routes.property import property_bp
from routes.booking import booking_bp
from routes.review import review_bp
from routes.messaging import messaging_bp
from routes.admin import admin_bp

app = Flask(__name__)
app.config.from_object(Config)

# Initialize the MongoDB database
db = MongoEngine(app)

# Register blueprints for different routes
app.register_blueprint(auth_bp, url_prefix='/api')
app.register_blueprint(property_bp, url_prefix='/api')
app.register_blueprint(booking_bp, url_prefix='/api')
app.register_blueprint(review_bp, url_prefix='/api')
app.register_blueprint(messaging_bp, url_prefix='/api')
app.register_blueprint(admin_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
