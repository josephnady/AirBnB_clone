#!/usr/bin/python3
import models
from models.base_model import BaseModel
from models.city import City


class State(BaseModel):
    """Representation of state """
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    @property
    def cities(self):
        """getter for list of city instances related to the state"""
        city_list = []
        all_cities = models.storage.all(City)
        for city in all_cities.values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
