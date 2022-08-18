from enum import Enum

class TeamType(Enum):
    """
    Enum for the different types of teams.
    """
    MEN = 1
    WOMEN = 2
    BOYS = 3
    GIRLS = 4

DATABASE = './data/database.db'
