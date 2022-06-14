import datetime

class Schedule:
    def __init__(self, days: str, time: datetime) -> None:
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