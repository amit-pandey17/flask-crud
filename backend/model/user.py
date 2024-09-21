from flask_sqlalchemy import SQLAlchemy
from backend.globals import ROLES  # Import the global roles

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    # Defining fields
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    role = db.Column(db.String(50), nullable=False)

    # Dictionary for receiving data
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'role': self.role
        }
    
# CRUD operations
class UserModel:
    # Read all users
    @staticmethod
    def get_all_users():
        return User.query.all()

    # Read user by ID
    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)
    
    # Create user
    @staticmethod
    def create_user(name, email, role):
        if role not in ROLES:  # Validate the role
            raise ValueError("Invalid role")
        
        new_user = User(name=name, email=email, role=role)
        db.session.add(new_user)
        db.session.commit()
        return new_user
    
    # Update user
    @staticmethod
    def update_user(user, name, email, role):
        if role not in ROLES:  # Validate the role
            raise ValueError("Invalid role")
        
        user.name = name
        user.email = email
        user.role = role
        db.session.commit()
        return user

    # Delete user
    @staticmethod
    def delete_user(user):
        db.session.delete(user)
        db.session.commit()