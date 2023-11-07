class BaseModel:
    """BaseModel class"""

class State(BaseModel):
    """State class"""
    name = ""

class City(BaseModel):
    """City class"""
    state_id = ""
    name = ""

class Amenity(BaseModel):
    """Amenity class"""
    name = ""

class Place(BaseModel):
    """Place class"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

class Review(BaseModel):
    """Review class"""
    place_id = ""
    user_id = ""
    text = ""