from fastapi import HTTPException
from models.feedback import Feedback

async def submit_feedback(feedback: Feedback):
    try:
        from main import feedback_collection
        
        feedback_data = feedback.dict()  # Convert Pydantic model to dictionary
        
        result = await feedback_collection.insert_one(feedback_data) # Insert the feedback data into MongoDB
        
        # Check if insertion was successful and return a response
        if result.inserted_id:
            print(f"Inserted feedback with ID: {result.inserted_id}")
            return {"success": True, "message": "Feedback submitted successfully."}
        else:
            raise HTTPException(status_code=400, detail="Failed to insert feedback.")
    
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="There was an error processing your feedback.")