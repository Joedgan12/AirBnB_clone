#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review.

    Attributes:
        place_id (str): Place id.
        user_id (str): User id.
        text (str): text for the review.
    """

    place_id = ""
    user_id = ""
    text = ""
