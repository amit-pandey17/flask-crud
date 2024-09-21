from fsa import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
#defining feilds
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200), nullable = False)
    email = db.Column(db.String(200), nullable = False, unique = True)
    role = db.Column(db.String(50), nullable = False)

    #dictionary for receiving data
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'role': self.role
        }
    
    #CRUD
class UserModel:
    #read all
    @staticmethod
    def get_all_users():
        return User.query.all()
    # read by id
    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)
    
    #create user
    @staticmethod
    def create_user(name, email, role):
        new_user = User(name = name, email = email, role = role)
        db.session.add(new_user)
        db.session.commit()
        return new_user
    
    #update user
    @staticmethod
    def update_user(user, name, email, role):
        user.name = name
        user.email = email
        user.role = role
        db.session.commit()
        return user

    #delete user
    @staticmethod
    def delete_user(user):
        db.session.delete(user)
        db.session.commit()