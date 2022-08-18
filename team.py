import player
from consts import TeamType

class Team:
    
    def __init__(self, id: str, name: str, type: TeamType, members: list['player.Player'] = [], active: bool = True) -> None:
        self.id = id
        self.name = name
        self.type = type
        self.members = members
        self.active = active
        
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
    def team_type(self) -> 'TeamType':
        return self.type
    
    @team_type.setter
    def team_type(self, value: 'TeamType') -> None:
        self.type = value
    
    @property
    def team_members(self) -> list['player.Player']:
        return self.members
    
    @team_members.setter
    def team_members(self, value) -> None:
        self.members = value
    
    def add_member(self, player: 'player.Player') -> None:
        self.members.append(player)
    
    def remove_member(self, player: 'player.Player') -> None:
        self.members.remove(player)
        
    def num_members(self) -> int:
        return len(self.members)
    
    def __str__(self) -> str:
        return f"name: {self.name} members: {self.members}"