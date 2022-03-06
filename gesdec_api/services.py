from pony.orm import db_session
from gesdec_api.schemas import FeedbackCreate
from gesdec_api.models import Feedback

@db_session
def create_feedback(feedback_ob: FeedbackCreate):
    Feedback(
        feedback=feedback_ob.feedback
    )
    
