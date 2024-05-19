#!/usr/bin/python3
"""define the city class of project."""

from models.base_model import BaseModel

class City(BaseModel):
    """This city class inherts from the base model class.
    Attributes:
    state_id(str) = the of the state.
    name (str ) = the name of the city.
    """
    state_id = ""
    name = ""