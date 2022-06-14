import datetime
import team

class Player:
        
    def __init__(self, id: str, firstName: str, lastName: str, team: str, date_of_birth: datetime, picture: str, active: bool = True) -> None:
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.team = team
        self.date_of_birth = date_of_birth
        self.picture = picture
        self.active = active
        
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
    def player_team(self) -> 'team.Team':
        return self.team
    
    @player_team.setter
    def player_team(self, value: 'team.Team') -> None:
        self.team = value
    
    @property
    def dob(self) -> datetime:
        return self.date_of_birth
    
    @dob.setter
    def dob(self, value: datetime) -> None:
        self.date_of_birth = value
        
    @property
    def picture(self) -> str:
        return self.picture
    
    @picture.setter
    def picture(self, value: str) -> None:
        self.picture = value
        
    @property
    def active(self) -> bool:
        return self.active
        
    def age(self) -> int:
        today = datetime.date.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
    
    def activate(self) -> None:
        self.active = True
    
    def deactivate(self) -> None:
        self.active = False
        
    def __str__(self) -> str:
        return f"first name: {self.firstName} last name: {self.lastName} team: {self.team} dob: {self.date_of_birth} active: {self.active}"
