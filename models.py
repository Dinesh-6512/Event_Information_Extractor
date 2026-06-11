from pydantic import BaseModel
from typing import List

class EventDetails(BaseModel):
    event_name: List[str]
    event_date: List[str]
    event_time: List[str]
    event_location: List[str]
    organizer: List[str]