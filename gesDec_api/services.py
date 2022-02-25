from pony.orm import db_session
from gesDec_api.schemas import FeedbackCreate
from gesDec_api.models import Feedback

@db_session
def create_feedback(feedback_ob: FeedbackCreate):
    Feedback(
        feedback=feedback_ob.feedback
    )
    
