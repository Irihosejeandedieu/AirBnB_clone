#!/usr/bin/python3
"""Defines the place """
from models.base_model import BaseModel

class Place (BaseModel):
    """The great representing the place class from BaseModel.
    name(str): the name of the client/ user.
    user_id(str): the id of the user.
    city_id (str): the id of the city.
    description (str): the description of the place..

    number_rooms (int): the number of the rooms in a place.
    max_guest (int): the maximum number of the guests at the place.
    number_bathrooms (int): the number of the bath rooms available at the place.
    price_by_nigth (int): the price for whole nigth at the place.
    latitude (float): the location of the place.

    longtude (float): the llocation of the place.
    amenity_ids (list): the list of Amenity ids. 
    """
    name = ""
    user_id = ""
    city_id = ""
    description = ""

    number_rooms = 0
    max_guests = 0
    number_bathrooms = 0
    price_by_nigth = 0

    latitude = 0.0
    longtude = 0.0
    amenity = []
