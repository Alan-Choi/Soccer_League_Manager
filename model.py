import datetime
import uuid
from constants import Type


class Player:
    
    def __init__(self, id: str, firstName: str, lastName: str, team: 'Team', date_of_birth: datetime) -> None:
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.team = team
        self.date_of_birth = date_of_birth
        self.active = True
        
    @property
    def player_id(self):
        return self.id
    
    @player_id.setter
    def player_id(self, value: str) -> None:
        self.id = value
    
    @property
    def first_name(self) -> str:
        return self.firstName
    
    @first_name.setter
    def first_name(self, value: str) -> None:
        self.firstName = value
        
    @property
    def last_name(self) -> str:
        return self.lastName
    
    @last_name.setter
    def last_name(self, value: str) -> None:
        self.lastName = value
    
    @property
    def player_team(self) -> 'Team':
        return self.team
    
    @player_team.setter
    def player_team(self, value: 'Team') -> None:
        self.team = value
    
    @property
    def dob(self) -> datetime:
        return self.date_of_birth
    
    @dob.setter
    def dob(self, value: datetime) -> None:
        self.date_of_birth = value
        
    def age(self) -> int:
        today = datetime.now()
        return today.year - self.date_of_birth.year
    
    def activate(self) -> None:
        self.active = True
    
    def deactivate(self) -> None:
        self.active = False
        
    def __str__(self) -> str:
        return f"first name: {self.firstName} last name: {self.lastName} team: {self.team} dob: {self.date_of_birth} active: {self.active}"
      
class Team:
    
    def __init__(self, id: str, name: str, type: 'Type'):
        self.id = id
        self.name = name
        self.type = type
        self.members: list['Player'] = []
        
    @property
    def team_id(self) -> str:
        return self.id
    
    @team_id.setter
    def team_id(self, value: str) -> None:
        self.id = value
    
    @property
    def team_name(self) -> str:
        return self.name
    
    @team_name.setter
    def team_name(self, value: str) -> None:
        self.name = value
        
    @property
    def team_type(self) -> 'Type':
        return self.type
    
    @team_type.setter
    def team_type(self, value: 'Type') -> None:
        self.type = value
    
    def members(self) -> list['Player']:
        return self.members
    
    def add_member(self, player: 'Player') -> None:
        self.members.append(player)
    
    def remove_member(self, player: 'Player') -> None:
        self.members.remove(player)
        
    def num_members(self) -> int:
        return len(self.members)
    
    def __str__(self) -> str:
        return f"name: {self.name} members: {self.members}"


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
    
        
class Referee:
    
    def __init__(self, id: str, firstName: str, lastName: str) -> None:
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.active = True
    
    @property
    def ref_id(self) -> str:
        return self.id
    
    @ref_id.setter
    def ref_id(self, value: str) -> None:
        self.id = value
    
    @property
    def first_name(self) -> str:
        return self.firstName
    
    @first_name.setter
    def first_name(self, value: str) -> None:
        self.firstName = value
    
    @property
    def last_name(self) -> str:
        return self.lastName
    
    @last_name.setter
    def last_name(self, value: str) -> None:
        self.lastName = value
    
    def activate(self) -> None:
        self.active = True
        
    def deactivate(self) -> None:
        self.active = False
        
    def __str__(self) -> str:
        return f"first name: {self.firstName} last name: {self.lastName} active: {self.active}"
    
class Schedule:
    def __init__(self, id: str, days: str, time: datetime) -> None:
        self.id = id
        self.days = days
        self.time = time
    
    @property
    def sched_id(self):
        return self.id
    
    @sched_id.setter
    def sched_id(self, value: str) -> None:
        self.id = value
        
    @property
    def days(self) -> str:
        return self.days
    
    @days.setter
    def days(self, value: str) -> None:
        self.days = value
    
    @property
    def time(self) -> datetime:
        return self.time
    
    @time.setter
    def time(self, value: datetime) -> None:
        self.time = value
