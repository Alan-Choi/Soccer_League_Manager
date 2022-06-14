import datetime
from team import Team
from referee import Referee

class Match:
    
    def __init__(self, id: str, date: datetime, team1: 'Team', team2: 'Team', score1: int, score2: int, referee: 'Referee') -> None:
        self.id = id
        self.date = date
        self.team1 = team1
        self.team2 = team2
        self.score1 = score1
        self.score2 = score2
        self.referee = referee
        
    @property
    def match_id(self):
        return self.id
    
    @match_id.setter
    def match_id(self, value: str) -> None:
        self.id = value
    
    @property
    def date(self) -> datetime:
        return self.date
    
    @date.setter
    def date(self, value: datetime) -> None:
        self.date = value
    
    @property
    def team1(self) -> 'Team':
        return self.team1
    
    @team1.setter
    def team1(self, value: 'Team') -> None:
        self.team1 = value
    
    @property
    def team2(self) -> 'Team':
        return self.team2
    
    @team2.setter
    def team2(self, value: 'Team') -> None:
        self.team2 = value
        
    @property
    def score1(self) -> int:
        return self.score1
    
    @score1.setter
    def score1(self, value: int) -> None:
        self.score1 = value
    
    @property
    def score2(self) -> int:
        return self.score2
    
    @score2.setter
    def score2(self, value: int) -> None:
        self.score2 = value
        
    @property
    def ref(self) -> 'Referee':
        return self.referee
    
    @ref.setter
    def ref(self, value: 'Referee') -> None:
        self.referee = value
    
    def winner(self) -> 'Team':
        if self.score1 > self.score2:
            return self.team1
        
        return self.team2
    
    def __str__(self) -> str:
        return f"date: {self.date} teams: {self.team1}, {self.team2} scores: {self.score1} : {self.score2} referee: {self.referee}"