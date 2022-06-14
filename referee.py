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