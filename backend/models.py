from app import db

# User Model
class User(db.Document):
    username = db.StringField(required=True, unique=True)
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True)
    is_host = db.BooleanField(default=False)

    def __repr__(self):
        return f"<User {self.username}>"

# Property Model
class Property(db.Document):
    title = db.StringField(required=True)
    description = db.StringField(required=True)
    location = db.StringField(required=True)
    price_per_night = db.FloatField(required=True)
    rating = db.FloatField(default=0.0)
    host = db.ReferenceField(User, reverse_delete_rule=db.CASCADE, required=True)

    def __repr__(self):
        return f"<Property {self.title}>"

# Booking Model
class Booking(db.Document):
    check_in_date = db.DateTimeField(required=True)
    check_out_date = db.DateTimeField(required=True)
    guest = db.ReferenceField(User, reverse_delete_rule=db.CASCADE, required=True)
    property = db.ReferenceField(Property, reverse_delete_rule=db.CASCADE, required=True)

    def __repr__(self):
        return f"<Booking {self.id}>"

# Review Model
class Review(db.Document):
    rating = db.FloatField(required=True)
    comment = db.StringField()
    guest = db.ReferenceField(User, reverse_delete_rule=db.CASCADE, required=True)
    property = db.ReferenceField(Property, reverse_delete_rule=db.CASCADE, required=True)

    def __repr__(self):
        return f"<Review {self.id}>"
