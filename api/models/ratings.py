from typing import Optional, List, Dict
from api.utils.firebase import db
from datetime import datetime

class Ratings:
    def __init__(
        self,
        place_id:str,
        user_id:str,
        name:str,
        username:str,
        rating:float,
        created_at: int,
                 ) -> None:
        self.place_id = place_id
        self.user_id = user_id
        self.name = name
        self.username = username
        self.rating = rating
        self.created_at = created_at
        
    def to_dict(self) -> Dict:
        return {
            'place_id': self.place_id,
            'user_id': self.user_id,
            'name': self.name,
            'username': self.username,
            'rating': self.rating,
            'created_at': self.created_at
        }
        
    @staticmethod
    def get_rating_by_place_id(place_id: str) -> Optional[Dict]:
        """
        Fetches a Place Rating object from the database using Place ID.
        Args:
            feature_id: The unique identifier of the feature
        Returns:
            Place Rating object if found, None otherwise
        """
        ratings_data = db.child("ratings").child(place_id).get().val()
        if ratings_data:
            rating = Ratings(
                place_id=ratings_data.get('place_id'),
                user_id=ratings_data.get('user_id'),
                name=ratings_data.get('name'),
                username=ratings_data.get('username'),
                rating=ratings_data.get('rating'),
                created_at=ratings_data.get('created_at')
            )
            return rating.to_dict()
        return None
        
    @staticmethod
    def add_rating(place_id: str, user_id: str, name: str, username: str, rating: float) -> Dict:
        """
        Adds a new rating for a place to the database.
        Args:
            place_id: The unique identifier of the place
            user_id: The unique identifier of the user
            name: The name of the user
            username: The username of the user
            rating: The rating value
        Returns:
            The newly created Ratings object
        """
        created_at = int(datetime.now().timestamp() * 1000)
        rating_data = {
            'place_id': place_id,
            'user_id': user_id,
            'name': name,
            'username': username,
            'rating': rating,
            'created_at': created_at
        }
        
        db.child("ratings").child(place_id).set(rating_data)
        
        rating = Ratings(
            place_id=place_id,
            user_id=user_id,
            name=name,
            username=username,
            rating=rating,
            created_at=created_at
        )
        return rating.to_dict()
    
    @staticmethod
    def add_to_favorites(user_id: str, place_id: str) -> Dict:
        """
        Adds a place to user's favorites list
        """
        timestamp = int(datetime.now().timestamp() * 1000)
        favorite_data = {
            'place_id': place_id,
            'added_at': timestamp
        }
        
        db.child("favorites").child(user_id).child(place_id).set(favorite_data)
        return favorite_data

    @staticmethod
    def remove_from_favorites(user_id: str, place_id: str) -> bool:
        """
        Removes a place from user's favorites list
        """
        db.child("favorites").child(user_id).child(place_id).remove()
        return True

    @staticmethod
    def get_user_favorites(user_id: str) -> List[Dict]:
        """
        Gets all favorite places for a user
        """
        favorites = db.child("favorites").child(user_id).get().val()
        if favorites:
            return [{'place_id': k, **v} for k, v in favorites.items()]
        return []
