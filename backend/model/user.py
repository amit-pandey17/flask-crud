from fsa import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
#defining feilds
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200), nullable = False)
    email = db.Column(db.String(200), nullable = False, unique = True)
    role = db.Column(db.String(50), nullable = False)

    #dictionary
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'role': self.role
        }
    
class UserModel:
    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)