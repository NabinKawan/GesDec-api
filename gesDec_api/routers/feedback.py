from fastapi import APIRouter, HTTPException
from gesDec_api.services import services
from gesDec_api.schemas import FeedbackCreate

router = APIRouter(prefix="/feedback", tags=["Feedback"])


@router.post("", response_model=str)
def post_feedback(feedback_ob: FeedbackCreate):
    services.create_feedback(feedback_ob=feedback_ob)
    return "success"
