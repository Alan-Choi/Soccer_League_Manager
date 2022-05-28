from enum import Enum

class Type(Enum):
    """
    Enum for the different types of teams.
    """
    MEN = 1
    WOMEN = 2
    BOYS = 3
    GIRLS = 4

DATABASE = 'database.db'