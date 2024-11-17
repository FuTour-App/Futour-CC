from flask_login import UserMixin
from typing import Optional
from api.utils.firebase import db

class User(UserMixin):
    def __init__(self, user_id: str, username: str, email: str) -> None:
        self.id = user_id
        self.username = username
        self.email = email
    
    @staticmethod
    def get_by_id(user_id: str) -> Optional['User']:
        """
        Args:
            user_id: The unique identifier of the user 
        Returns:
            User object if found, None otherwise
        """
        user_data = db.child("users").child(user_id).get().val()
        if user_data:
            return User(
                user_id=user_id,
                username=user_data.get('username'),
                email=user_data.get('email')
            )
        return None
