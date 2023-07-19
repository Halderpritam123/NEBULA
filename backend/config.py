import os
from datetime import timedelta

class Config:
    # Other configurations...
    
    # JWT Configuration
    JWT_SECRET_KEY = 'your-jwt-secret-key'  # Replace with your own JWT secret key
    JWT_ALGORITHM = 'HS256'
    JWT_EXPIRATION_DELTA = timedelta(days=1)  # Set the token expiration time as needed

    # MongoDB Configuration
    MONGODB_SETTINGS = {
        'host': 'your-mongodb-uri',  # Replace with your MongoDB URI
        'db': 'your-database-name',   # Replace with your database name
    }
