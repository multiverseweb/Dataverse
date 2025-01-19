from fastapi import APIRouter, Form
from schema.feedback import submit_feedback
from models.feedback import Feedback

router = APIRouter()

@router.post("/submit_feedback")
async def submit_feedback_route(
    Name: str = Form(...),
    Email: str = Form(...),
    Message: str = Form(...),
    Rating: int = Form(...),
):
    # Convert the raw data into a Pydantic model
    feedback = Feedback(Name=Name, Email=Email, Message=Message, Rating=Rating)

    return await submit_feedback(feedback)