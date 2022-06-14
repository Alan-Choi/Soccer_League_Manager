import consts
import sqlite3
from model import Model
from view import View
from player import Player
from team import Team
from match import Match
from referee import Referee
from schedule import Schedule


class Controller:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
    
    def initialize_database(self):
        self.model.initialize_database()