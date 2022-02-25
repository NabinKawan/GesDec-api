from pony.orm import db_session
from schemas import FeedbackCreate
from models import Feedback

@db_session
def create_feedback(feedback_ob: FeedbackCreate):
    Feedback(
        feedback=feedback_ob.feedback
    )
    
