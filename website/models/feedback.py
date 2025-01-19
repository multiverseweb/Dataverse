from pydantic import BaseModel
class Feedback(BaseModel):
    Name: str
    Email: str
    Message: str
    Rating: int