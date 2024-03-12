#!/usr/bin/python3
"""Amenity class is defined."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """an amenity is represented.

    Attributes:
        name (str): name of the amenity.
    """

    name = ""
