from sqlalchemy.orm import sessionmaker
from models_user import User, SessionUser

class UserService:
    def __init__(self):
        self.db = SessionUser()

    def register_user(self, email, frequency):
        user = User(email=email, frequency=frequency)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def unsubscribe_user(self, email):
        user = self.db.query(User).filter(User.email == email).first()
        if user:
            self.db.delete(user)
            self.db.commit()
            return True
        return False

    def get_all_users(self):
        return self.db.query(User).all()