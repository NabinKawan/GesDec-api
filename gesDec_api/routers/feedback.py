from fastapi import APIRouter, HTTPException
import services
from schemas import FeedbackCreate

router = APIRouter(prefix="/feedback", tags=["Feedback"])


@router.post("", response_model=str)
def post_feedback(feedback_ob: FeedbackCreate):
    services.create_feedback(feedback_ob=feedback_ob)
    return "success"
