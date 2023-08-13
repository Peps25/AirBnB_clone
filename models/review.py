#!/usr/bin/python3

from model.base_model import BaseModel

class Review(BaseModel):
    """This represents a review"""

    place_id = ""
    user_id = ""
    text = ""
